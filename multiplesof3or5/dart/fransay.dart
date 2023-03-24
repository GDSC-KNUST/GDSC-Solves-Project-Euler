// AUTHOR: Fransay
// DATE: 24/03/23
// DESCRIPTION: A program that returns the sum of multiples of 3 or 5 below 1000.

const numberLimit = 1000; 
void main(){
    var sum = 0;
    for (int i=0; i<numberLimit;i++){
        if (i%3 ==0 || i%5 == 0){
            sum+=i;
        }
    }
    print(sum);
}