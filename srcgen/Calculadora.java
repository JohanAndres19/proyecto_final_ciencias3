public class Calculadora {
  
  private int x;
  
  private int y;

  public Calculadora(int x , int y){
    this.x=x;
    this.y=y;
    this.sumar();
    this.restar();
    this.multiplicar();
    this.division();
  }
  
  
  public void sumar(){
    System.out.println(x + y);
  }
  
  
  public void restar(){
    System.out.println(x - y);
  }
  
  
  public void multiplicar(){
    System.out.println(x * y);
  }
  
  
  public void division(){
    System.out.println(x / y);
  }
  
  public static void main(String[] args) {
    new Calculadora(4,5);        
  }
  
}