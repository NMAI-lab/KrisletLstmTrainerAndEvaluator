//import org.apache.commons.io.FileUtils;
//import org.apache.commons.io.FilenameUtils;
//import org.deeplearning4j.nn.graph.ComputationGraph;
//import org.deeplearning4j.nn.modelimport.keras.KerasLayer;
import org.deeplearning4j.nn.modelimport.keras.KerasModelImport;
import org.nd4j.linalg.api.ndarray.INDArray;
import org.nd4j.linalg.factory.Nd4j;
import org.deeplearning4j.nn.multilayer.MultiLayerNetwork;

//import java.io.File;
//import java.net.URL;

//import static java.io.File.createTempFile;

/**
 * Test import of DeepMoji application
 *
 * @author Max Pumperla
 */
public class Main {

    //public static final String DATA_PATH = FilenameUtils.concat(System.getProperty("java.io.tmpdir"),
    //  "dl4j_keras/");
    //public static final String DATA_PATH = "C:\\Users\\Patrick\\Desktop";



    public static void main(String[] args) throws Exception {
        MultiLayerNetwork model = KerasModelImport.importKerasSequentialModelAndWeights("C:\\Users\\Patrick\\Documents\\GitHub\\KrisletLstmTrainerAndEvaluator\\Krislet_dl4j\\models\\model.h5");
        System.out.println(model.summary());
        System.out.println("Example completed.");
    }
}
