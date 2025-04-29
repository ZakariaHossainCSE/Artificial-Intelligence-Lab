import java.util.*;

public class GeneticSolver {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int T, k;
        System.out.println("Enter target T:");
        T = sc.nextInt();

        System.out.println("Enter list length k:");
        k = sc.nextInt();

        GA ga = new GA(T, k);
        ga.run();
    }
}

class GA {
    Population population;
    Individual fittest, secondFittest;
    int generationCount;
    int T, k;
    Random rn = new Random();

    GA(int T, int k) {
        this.T = T;
        this.k = k;
        this.generationCount = 0;
        this.population = new Population(10, k, T); // 10 individuals
        this.population.calculateFitness();
    }

    void run() {
        while (population.fittest < 10) {
            generationCount++;

            selection();
            crossover();
            if (rn.nextInt(10) < 7) mutation(); // 70% chance
            addFittestOffspring();
            population.calculateFitness();
        }

        System.out.println("\nCase#" + generationCount + " Output:");
        Individual best = population.getFittest();
        for (int i = 0; i < k; i++) {
            System.out.print(best.genes[i] + " ");
        }
        System.out.println();
    }

    void selection() {
        fittest = population.getFittest();
        secondFittest = population.getSecondFittest();
    }

    void crossover() {
        int point = rn.nextInt(2); // crossover only first two genes
        for (int i = 0; i < point; i++) {
            int temp = fittest.genes[i];
            fittest.genes[i] = secondFittest.genes[i];
            secondFittest.genes[i] = temp;
        }
    }

    void mutation() {
        int mp1 = rn.nextInt(2); // mutate only first two positions
        fittest.genes[mp1] = rn.nextInt(10);
        int mp2 = rn.nextInt(2);
        secondFittest.genes[mp2] = rn.nextInt(10);
    }

    void addFittestOffspring() {
        fittest.calcFitness(T);
        secondFittest.calcFitness(T);
        int leastIdx = population.getLeastFittestIndex();
        population.individuals[leastIdx] = getFittestOffspring();
    }

    Individual getFittestOffspring() {
        return fittest.fitness > secondFittest.fitness ? fittest : secondFittest;
    }
}

class Individual {
    int[] genes;
    int fitness = 0;
    int k;
    Random rn = new Random();

    Individual(int k) {
        this.k = k;
        genes = new int[k];
        for (int i = 0; i < k; i++) {
            if (i < 2)
                genes[i] = rn.nextInt(10); // First 2 positions vary
            else
                genes[i] = 0;              // Rest are always 0
        }
    }

    void calcFitness(int T) {
        int sum = genes[0] + genes[1];
        fitness = (sum == T) ? 10 : 10 - Math.abs(T - sum);
    }
}

class Population {
    int popSize;
    Individual[] individuals;
    int fittest = 0;
    int k, T;

    Population(int popSize, int k, int T) {
        this.popSize = popSize;
        this.k = k;
        this.T = T;
        individuals = new Individual[popSize];
        for (int i = 0; i < popSize; i++) {
            individuals[i] = new Individual(k);
        }
    }

    void calculateFitness() {
        for (Individual ind : individuals) {
            ind.calcFitness(T);
        }
        getFittest();
    }

    Individual getFittest() {
        int maxFit = -1, idx = 0;
        for (int i = 0; i < popSize; i++) {
            if (individuals[i].fitness > maxFit) {
                maxFit = individuals[i].fitness;
                idx = i;
            }
        }
        fittest = individuals[idx].fitness;
        return individuals[idx];
    }

    Individual getSecondFittest() {
        int max1 = 0, max2 = 1;
        if (individuals[max2].fitness > individuals[max1].fitness) {
            int temp = max1;
            max1 = max2;
            max2 = temp;
        }
        for (int i = 2; i < popSize; i++) {
            if (individuals[i].fitness > individuals[max1].fitness) {
                max2 = max1;
                max1 = i;
            } else if (individuals[i].fitness > individuals[max2].fitness) {
                max2 = i;
            }
        }
        return individuals[max2];
    }

    int getLeastFittestIndex() {
        int minFit = Integer.MAX_VALUE, idx = 0;
        for (int i = 0; i < popSize; i++) {
            if (individuals[i].fitness < minFit) {
                minFit = individuals[i].fitness;
                idx = i;
            }
        }
        return idx;
    }
}
