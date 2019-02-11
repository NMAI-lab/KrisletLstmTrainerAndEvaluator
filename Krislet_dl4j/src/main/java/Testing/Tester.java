package Testing;

import Behaviour.Behaviour;
import KrisletDemo.BehaviourModel;
import org.nd4j.evaluation.classification.Evaluation;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Tester {

    public static void main(String [] a) {
        System.out.println("This is the test routine");

        BehaviourModel behaviourModel = new BehaviourModel("FiniteTurnDense");


        String line;
        String cvsSplitBy = ",";
        String csvFile = "FiniteTurnKrislet.csv";
        List<Double> ballDistance = new ArrayList<>();
        List<Double> ballDirection = new ArrayList<>();
        List<Double> goalDistance = new ArrayList<>();
        List<Double> goalDirection = new ArrayList<>();
        List<Double> action = new ArrayList<>();

        try (BufferedReader br = new BufferedReader(new FileReader(csvFile))) {

            boolean firstLine = true;
            while ((line = br.readLine()) != null) {

                // use comma as separator
                String[] dataLine = line.split(cvsSplitBy);

                if (!firstLine) {
                    ballDistance.add(Double.valueOf(dataLine[0]));
                    ballDirection.add(Double.valueOf(dataLine[1]));
                    goalDistance.add(Double.valueOf(dataLine[2]));
                    goalDirection.add(Double.valueOf(dataLine[3]));
                    action.add(Double.valueOf(dataLine[4]));
                } else {
                    firstLine = false;
                }
            }

        } catch (IOException e) {
            e.printStackTrace();
        }

        Evaluation eval = new Evaluation(4);
        double maxI = 0.2 * action.size();
        for (int i = 0; i < maxI; i++) {

            // Generate the prediction
            int trueAction = action.get(i).intValue();
            double currentBallDistance = ballDistance.get(i);
            double currentBallDirection = ballDirection.get(i);
            double currentGoalDistance = goalDistance.get(i);
            double currentGoalDirection = goalDirection.get(i);
            int predictedAction = behaviourModel.getAction(currentBallDistance, currentBallDirection, currentGoalDistance, currentGoalDirection);

            // Log the result
            eval.eval(trueAction, predictedAction);
        }

        double fTurnP = eval.f1(Behaviour.turnP);
        double fTurnN = eval.f1(Behaviour.turnN);
        double fDash = eval.f1(Behaviour.dash);
        double fKick = eval.f1(Behaviour.kick);
        System.out.println("F Measure Turn+: " + fTurnP);
        System.out.println("F Measure Turn-: " + fTurnN);
        System.out.println("F Measure Dash: " + fDash);
        System.out.println("F Measure Kick: " + fKick);

        System.out.println(eval.stats());
    }
}
