#ifndef SERVOMOTOR_H
#define SERVOMOTOR_H
#include <Arduino.h>
#include <Servo.h>

class ServoMotor
{
  public:
    ServoMotor();
    void setup(int pinEsquerda, int pinDireita);
    void frente();
    void viraDireita();
    void viraEsquerda();
    void re();
    void parado();
    void calibra(int pEsq, int pDir);

  private:
    int paradoDireito = 1500;
    int paradoEsquerdo = 1500;
    int intensidade;
    int pinEsq, pinDir;

    Servo mEsquerdo;
    Servo mDireito;
};

#endif
