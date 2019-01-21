package KrisletDemo;

import org.deeplearning4j.nn.modelimport.keras.KerasModelImport;
import org.nd4j.linalg.api.ndarray.INDArray;
import org.nd4j.linalg.factory.Nd4j;
import org.deeplearning4j.nn.multilayer.MultiLayerNetwork;
import org.nd4j.linalg.util.ArrayUtil;


public class BehaviourModel {
    // Finite Turn LSTM
    //private String modelFile = "models\\FiniteTurn\\LSTM1.h5";
    //private final int depth = 120;

    // Finite Turn Dense
    //private String modelFile = "models\\FiniteTurn\\Dense1.h5";
    //private final int depth = 0;

    // State Based Kick Spin LSTM
    //private String modelFile = "models\\StateBasedKickSpin\\LSTM1.h5";
    //private final int depth = 120;

    // State Based Kick Spin Dense
    //private String modelFile = "models\\StateBasedKickSpin\\Dense1.h5";
    //private final int depth = 0;

    // State Based Turn Direction LSTM
    //private String modelFile = "models\\StateBasedTurnDirection\\LSTM1.h5";
    //private final int depth = 120;

    // State Based Turn Direction  Dense
    private String modelFile = "models\\StateBasedTurnDirection\\Dense1.h5";
    private final int depth = 0;

    private double history[][];
    private int numFeatures = 4;
    private MultiLayerNetwork model;

    /**
     * Load the behaviour model
     */
    public BehaviourModel() {
        try {
            this.model = KerasModelImport.importKerasSequentialModelAndWeights(modelFile);
        } catch (Exception e) {
            System.out.println("Exception occured: " + e.toString());
        }

        if (this.depth != 0) {
            this.numFeatures = this.numFeatures + 1;
            this.history = new double[this.numFeatures][this.depth];
            for (int i = 0; i < this.numFeatures; i++) {
                for (int j = 0; j < this.depth; j++) {
                    this.history[i][j] = 0;
                }
            }
        }
    }

    /**
     * Get the action that goes with the current input
     * @param ballDistance
     * @param ballDirection
     * @param goalDistance
     * @param goalDirection
     * @return
     */
    public int getAction(double ballDistance, double ballDirection, double goalDistance, double goalDirection) {
        INDArray input = this.generateInput(ballDistance, ballDirection, goalDistance, goalDirection);
        int result = model.predict(input)[0];
        this.logHistory(result);
        return result;
    }

    /**
     * Genearate the input for the model
     * @param ballDistance
     * @param ballDirection
     * @param goalDistance
     * @param goalDirection
     * @return
     */
    private INDArray generateInput(double ballDistance, double ballDirection, double goalDistance, double goalDirection) {
        INDArray data;
        if (this.depth == 0) {
            double rawData[] = {ballDistance, ballDirection, goalDistance, goalDirection};
            data = Nd4j.create(rawData);
        } else {
            this.history[0][this.depth-1] = ballDistance;
            this.history[1][this.depth-1] = ballDirection;
            this.history[2][this.depth-1] = goalDistance;
            this.history[3][this.depth-1] = goalDirection;

            double[] flat = ArrayUtil.flattenDoubleArray(history);
            int[] shape = {1, this.numFeatures, this.depth};
            data = Nd4j.create(flat, shape, 'c');
        }
        return data;
    }

    /**
     * Shift everything in the history and add the last action
     * @param action
     */
    private void logHistory(int action) {
        // Only need to do something if the depth is not 0
        if (this.depth == 0) {
            return;
        }

        // Shift the features back in history
        for (int i = 0; i < this.numFeatures; i++) {
            for (int j = 0; j < (this.depth - 1); j++) {
                this.history[i][j] = this.history[i][j + 1];
            }
        }

        // Record the last action
        this.history[this.numFeatures-1][this.depth-1] = action;
    }
}
