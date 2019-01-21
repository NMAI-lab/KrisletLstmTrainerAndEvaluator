package org.deeplearning4j.examples.modelimport.keras;

//import org.apache.commons.io.FileUtils;
//import org.apache.commons.io.FilenameUtils;
//import org.deeplearning4j.nn.api.layers.LayerConstraint;
//import org.deeplearning4j.nn.graph.ComputationGraph;
//import org.deeplearning4j.nn.modelimport.keras.KerasLayer;
//import org.deeplearning4j.nn.modelimport.keras.KerasModelImport;
//import org.nd4j.linalg.api.ndarray.INDArray;
//import org.nd4j.linalg.api.ndarray.SparseFormat;
//import org.nd4j.linalg.factory.Nd4j;
//import org.deeplearning4j.nn.multilayer.MultiLayerNetwork;

//import java.io.File;
//import java.net.URL;
//import java.util.*;

//import static java.io.File.createTempFile;

/**
 * Test import of DeepMoji application
 *
 * @author Max Pumperla
 */
public class ImportDeepMoji {

    public static void main(String[] args) throws Exception {

        BehaviourModel model = new BehaviourModel();
        double ballDistance = Math.random() * 20;
        double ballDirection = Math.random() * 20;
        double goalDistance = Math.random() * 20;
        double goalDirection = Math.random() * 20;
        int action = model.getAction(ballDistance, ballDirection, goalDistance, goalDirection);
        // actions correspond to ['turn+','turn-', 'dash', 'kick']
    }
}
