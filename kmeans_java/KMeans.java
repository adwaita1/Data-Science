import java.util.Scanner;
import  java.lang.Math;
import java.text.DecimalFormat;

public class KMeans {
	int l,a[][],att,el,cst;
	double c[][];
	int cc[];
	Scanner sc;
	public KMeans() {
		sc=new Scanner(System.in);
		System.out.print("Enter Number of Elements : ");
		el=sc.nextInt();
		System.out.print("Enter Number of Attribute : ");
		att=sc.nextInt();
		a=new int[el][att];
		for (int i = 0; i < el; i++) {
			System.out.println("Enter "+att+" Attributes of "+(char)(65+i));
			for (int j = 0; j < att; j++) {
				a[i][j]=sc.nextInt();
			}
		}
		System.out.print(" \t");
		for (int j = 1; j <= att; j++) {
			System.out.print("att"+j+"\t");
		}
		System.out.println();
		for (int i = 0; i < el; i++) {
			System.out.print((char)(65+i)+"\t");
			for (int j = 0; j < att; j++) {
				System.out.print(" "+a[i][j]+"\t");
			}
			System.out.println();
		}
	}
	public void campare(double d[][]){
		int i;
		double tmp=999.99;
		for (int j = 0; j < el; j++) {
			tmp=999.99;
			for(i=0;i<cst;i++){
				if(d[j][i]<tmp){
					cc[j]=i;
					tmp=d[j][i];
				}
			}
		}
	}
	public void algo(){
		System.out.print("Enter Number of clusters : ");
		cst=sc.nextInt();
		c=new double[cst][att];
		cc=new int[el];
		for(int i=0;i<el;i++){
			cc[i]=0;
		}
		int oldcc[]=new int[el];
		double d[][]=new double[el][cst];
		for (int j = 0; j < att; j++) {
			for (int i = 0; i < cst; i++) {
				c[i][j]=a[i][j];
			}
		}
		do{
			for(int i=0;i<el;i++){
				oldcc[i]=cc[i];
			}
			for (int i = 0; i < el; i++) {
				for (int j = 0; j < cst; j++) {
					d[i][j]=0;
					for(int k=0;k<att;k++){
						d[i][j]=d[i][j]+(c[j][k]-a[i][k])*(c[j][k]-a[i][k]);
					}
					d[i][j]=Math.sqrt(d[i][j]);
				}
			}
			campare(d);//Adding to clusters
			int m=0;
			for(int cl=0;cl<cst;cl++){
				m=0;
				for (int i = 0; i < att; i++) {
					c[cl][i]=0;
				}
				System.out.print("Entries of Cluster "+(cl+1)+" : ");
				for (int j = 0; j < el; j++) {
					if(cc[j]==cl){
						System.out.print((char)(65+j)+" ");
						for (int i = 0; i < att; i++) {
							c[cl][i]=c[cl][i]+a[j][i];
						}
						m++;
					}
				}
				for (int i = 0; i < att; i++) {
					c[cl][i]=c[cl][i]/m;
				}
				System.out.println();
			}
			for (l = 0; l < el; l++) {
				if(cc[l]!=oldcc[l]){
					break;
				}
			}
			if(l!=el){
				for(int i=0;i<cst;i++){
					System.out.print("New Cluster "+(i+1)+":\t");
					for(int j=0;j<att;j++){
						System.out.print(new DecimalFormat("##.##").format(c[i][j])+"\t");
					}
					System.out.println();
				}
			}
		}
		while(l!=el);
	}
	public static void main(String[] args) {
		new KMeans().algo();
	}
}

