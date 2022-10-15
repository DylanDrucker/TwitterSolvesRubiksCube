#include <iostream>
#include <SFML/Graphics.hpp>
#include <cmath>
#include <fstream>

constexpr int dimension = 3;
constexpr int face_num = 3;
constexpr float length = 100;

struct Vector{
float x;
float y;
void rotate(float angle){
    float xx = std::cos(angle)*x + std::sin(angle)*y;
    float yy = -std::sin(angle)*x + std::cos(angle)*y;
    x =xx;
    y =yy;
}
};

enum class Colours{WHITE, YELLOW, RED, BLUE, ORANGE, GREEN};
class Square{
public:
    Square(){
        for(int& i : square){
            i = 0;
        }
    }

    explicit Square(const std::string& input){
        for(int i = 0; i < square.size(); i++){
            int k = input[i] - '0';
            square[i] = k;
        }
    }

    int get_num(int index){
        return square[index];
    }

    void update_square(std::string& input){
        for(int i = 0; i < square.size(); i++){
            int k = input[i] - '0';
            square[i] = k;
        }
    }

private:
    std::array<int,dimension*dimension> square{};
};
class Net{
public:
    Net(){
        for(int i = 0; i < face_num; i++){
            net[i] = Square{};
        }
    }
    std::array<Square,face_num> net{};
};

class DrawSquare : public sf::Drawable{
public :
    explicit DrawSquare(Square& square) : sq(square){
    int count = 0;

        for(int j = 0; j < dimension; j++) {
            for (int i = 0; i < dimension; i++) {
                float y_position = j*length;

                squares[count*4].position = sf::Vector2f{ i*length, y_position};
                squares[count*4 + 1].position = sf::Vector2f{i*length + length, y_position};
                squares[count * 4 + 2].position = sf::Vector2f{i*length + length, y_position+length};
                squares[count*4 + 3].position = sf::Vector2f{i*length, y_position + length};
                count++;

            }
        }
}

void skew(){
    float x = length * sqrt(3.0/4);
    float y = length * 0.5;
    int count = 0;
    for(int j = 0; j < dimension*dimension; j++){
       if(count % dimension != 0){
           squares[4*j].position.y = squares[4*j-3].position.y;
           squares[4*j].position.x = squares[4*j-3].position.x;
           squares[4*j + 3].position.y = squares[4*j-2].position.y;
           squares[4*j+3].position.x = squares[4*j-2].position.x;
       }
        squares[4*j+1].position.y = squares[4*j+1].position.y  - (count%dimension + 1) *y;
        squares[4*j+1].position.x = squares[4*j+1].position.x  - (count%dimension + 1) *(length-x);
        squares[4*j + 2].position.y = squares[4*j+2].position.y  - (count%dimension +1) *y;
        squares[4*j+2].position.x = squares[4*j+2].position.x  - (count%dimension + 1) *(length-x);
        count++;
    }
}

void mirror(){
    for (int i = 0; i < squares.getVertexCount(); i++){
        float dist = squares[i].position.x - squares[0].position.x;
        squares[i].position.x = squares[i].position.x - 2*dist;
    }
}

void mirror_diagonal(){
    int count = 0;
    for(int i = 0; i < squares.getVertexCount(); i++ ){
        float xx = squares[i].position.x - squares[0].position.x;
        float yy = squares[i].position.y - squares[0].position.y;
        Vector v{xx,yy};
        v.rotate(120 * M_PI/180);
        squares[i].position.x = v.x + squares[0].position.x;
        squares[i].position.y = v.y + squares[0].position.y;
    }
}





void change_square_color(int i, sf::Color colour){
    squares[4*i].color = colour;
    squares[4*i + 1].color = colour;
    squares[4*i + 2].color = colour;
    squares[4*i + 3].color = colour;
}



void update_colours(){
    for(int i = 0; i < dimension*dimension; i++){
        switch(sq.get_num(i)){
            case 0 :
                change_square_color(i, sf::Color::White);
                break;
            case 1 :
                change_square_color(i, sf::Color::Yellow);
                break;
            case 2 :
                change_square_color(i, sf::Color::Red);
                break;
            case 3:
                change_square_color(i, sf::Color::Blue);
                break;
            case 4:
                change_square_color(i, sf::Color::Magenta);
                break;
            case 5:
                change_square_color(i,sf::Color::Green);
                break;
        }
    }
}

void move_square(float x, float y){
    for(int i = 0; i < squares.getVertexCount(); i++){
        squares[i].position = sf::Vector2f{ squares[i].position.x + x,squares[i].position.y +y };
    }
}

    void draw(sf::RenderTarget &target, sf::RenderStates states) const override{
        target.draw(squares,states);
    };

    Square& sq;
    sf::VertexArray squares{sf::Quads, dimension*dimension*4};
};

class DrawNet : public sf::Drawable {
public:
    explicit DrawNet(Net &n, bool t) : net(n), top(t) {
        for(int i = 0; i<face_num; i++){
            squares.emplace_back(DrawSquare{net.net[i]});
        }
        squares[0].move_square(500,500);
        squares[0].skew();
        squares[0].mirror_diagonal();
        squares[1].move_square(500,500);
        squares[1].skew();
        squares[1].mirror();
        squares[2].move_square(500,500);
        squares[2].skew();

    }
    void MoveNet(float x, float y){
        for(int i = 0; i < face_num; i++){
           squares[i].move_square(x,y);
        }
    }
    void update_net(std::string& s){
            std::string top_s = s.substr(0,9);
            std::string left_s = s.substr(9,9);
            std::string right_s = s.substr(18,9);

            squares[0].sq.update_square(top_s);
            squares[0].update_colours();
            squares[1].sq.update_square(left_s);
            squares[2].sq.update_square(right_s);
            squares[1].update_colours();
            squares[2].update_colours();



    }


    void draw(sf::RenderTarget &target, sf::RenderStates states) const override{
        for(int i  = 0; i < face_num; i++){
            target.draw(squares[i]);
        }
    };

private:
    Net& net;
    std::vector<DrawSquare> squares{};
    bool top;
};



int main() {
    sf::RenderWindow window(sf::VideoMode::getDesktopMode(), "Rubik's Cube");
    std::ifstream myfile;
    myfile.open ("cubeStatus.txt");
    std::string sss;
    std::string str1;
    while(getline(myfile,str1)){
        sss += str1;
    }
    myfile.close();
    std::string ss = "123412341";
    sf::Image image;
    sf::RenderTexture texture;
    texture.create(window.getSize().x, window.getSize().y);
    image = window.capture();
    image.saveToFile( "screen.png" );
    Square sq{ss};
    Square sq2{ss};
    DrawSquare dsq2{sq2};
    DrawSquare dsq3{sq};
    DrawSquare dsq{sq};
    dsq.move_square(window.getSize().x/2,500);
    dsq2.move_square(window.getSize().x/2,500);
    dsq3.move_square(window.getSize().x/2,500);
    dsq.skew();
    dsq.mirror();
    dsq2.skew();
    dsq2.mirror_diagonal();
    dsq3.skew();
    Net n{};
    DrawNet nn{n,true};
    Net n2{};
    DrawNet nn2{n2,false};

    nn2.MoveNet(800,0);

    while(window.isOpen()){
        window.clear();
        sf::Event event;
        while(window.pollEvent(event)){
            if(event.type == sf::Event::Closed){
                /*texture.draw(dsq3);
                texture.draw(dsq);
                texture.draw(dsq2);
                auto capturedTexture = texture.getTexture();
                auto toSave = capturedTexture.copyToImage();
                toSave.saveToFile("output.png");*/
                window.close();
            }
        }
        myfile.open ("cubeStatus.txt");
        std::string str = "";
        sss.clear();
        while(getline(myfile,str)){
            sss += str;
        }
        for(int i = 0; i < sss.length(); i++){
            char c = sss[i];
            switch( c){
                case 'w' :
                    sss[i] = '0';
                    break;
                case 'y' :
                    sss[i] = '1';
                    break;
                case 'r' :
                    sss[i] = '2';
                    break;
                case 'b' :
                    sss[i] = '3';
                    break;
                case 'o' :
                    sss[i] = '4';
                    break;
                case 'g' :
                    sss[i] = '5';
                    break;
            }
        }
        std::string face1 = sss.substr(18,9);
        std::string correct = face1.substr(6,1) + face1.substr(3,1) +face1.substr(0,1) +  face1.substr(7,1) + face1.substr(4,1) + face1.substr(1,1) + face1.substr(8,1)+face1.substr(5,1) +face1.substr(2,1);
        std::string  face2 = sss.substr(9,9);

        std::string correct2 = face2.substr(0,1) + face2.substr(3,1) +face2.substr(6,1) +  face2.substr(1,1) + face2.substr(4,1) + face2.substr(7,1) + face2.substr(2,1)+face2.substr(5,1) +face2.substr(8,1);
      std::string face3 = sss.substr(0,9);

        std::string correct3 = face3.substr(8,1) + face3.substr(7,1) +face3.substr(6,1) +  face3.substr(5,1) + face3.substr(4,1) + face3.substr(3,1) + face3.substr(2,1)+face3.substr(1,1) +face3.substr(0,1);
        myfile.close();
        std::string s_top = correct3 + correct2 + correct;

         face1 = sss.substr(27,9);
        face3 = sss.substr(45,9);
        face2 = sss.substr(36,9);
       correct = face1.substr(6,1) + face1.substr(3,1) +face1.substr(0,1) +  face1.substr(7,1) + face1.substr(4,1) + face1.substr(1,1) + face1.substr(8,1)+face1.substr(5,1) +face1.substr(2,1);
         correct2 = face2.substr(0,1) + face2.substr(3,1) +face2.substr(6,1) +  face2.substr(1,1) + face2.substr(4,1) + face2.substr(7,1) + face2.substr(2,1)+face2.substr(5,1) +face2.substr(8,1);
        correct3 =face3.substr(8,1) + face3.substr(7,1) +face3.substr(6,1) +  face3.substr(5,1) + face3.substr(4,1) + face3.substr(3,1) + face3.substr(2,1)+face3.substr(1,1) +face3.substr(0,1);

        std::string s_bottom = correct3 + correct+ correct2;
        nn.update_net(s_top);
        nn2.update_net(s_bottom);
        dsq.update_colours();
        dsq2.update_colours();
        dsq3.update_colours();
       window.draw(nn);
        window.draw(nn2);
        window.display();
    }
    return 0;
}
