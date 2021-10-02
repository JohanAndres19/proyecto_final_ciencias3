public class Calculadora {
      private int x;
      private int y;

      public Calculadora(int x,int y,int z){
            this.x = x;
            this.y = y;
      }

      public void sumar(){
        System.out.println(x + y + 0);
      }

      public void restar(){
        System.out.println(x - y - 0);
      }

      public void multiplicar(){
        System.out.println(x * y * 1);
      }

      public void division(){
        System.out.println(x / y / 1);
      }

      public static void main(String[] args) {
        Calculadora a = new Calculadora(10,5,0);
        a.sumar();
        a.restar();
        a.multiplicar();
        a.division();
      }
}