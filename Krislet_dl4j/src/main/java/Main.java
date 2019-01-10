//import org.apache.commons.io.FileUtils;
//import org.apache.commons.io.FilenameUtils;
//import org.deeplearning4j.nn.graph.ComputationGraph;
//import org.deeplearning4j.nn.modelimport.keras.KerasLayer;
import org.deeplearning4j.nn.modelimport.keras.KerasModelImport;
//import org.nd4j.linalg.api.ndarray.INDArray;
//import org.nd4j.linalg.factory.Nd4j;
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


        // First, register the Keras layer wrapped around our custom SameDiff attention layer
        //KerasLayer.registerCustomLayer("AttentionWeightedAverage", KerasDeepMojiAttention.class);

        // Then, download the model from azure (check if it's cached)
        //File directory = new File(DATA_PATH);
        //if(!directory.exists()) directory.mkdir();

        //String modelUrl = "http://blob.deeplearning4j.org/models/deepmoji.h5";
        //String filePath = DATA_PATH + "model.h5";
        //File cachedKerasFile = new File(filePath);

        //if (!cachedKerasFile.exists()) {
        //    System.out.println("Downloading model to " + cachedKerasFile.toString());
        //    FileUtils.copyURLToFile(new URL(modelUrl), cachedKerasFile);
        //    System.out.println("Download complete");
        //    cachedKerasFile.deleteOnExit();
        //}

        // Finally, import the model and test on artificial input data.
        //ComputationGraph graph = KerasModelImport.importKerasModelAndWeights(cachedKerasFile.getAbsolutePath());
        //ComputationGraph graph = KerasModelImport.importKerasModelAndWeights(new ClassPathResource("C:\\Users\\Patrick\\Desktop\\model.h5"));
        //INDArray input = Nd4j.create(new int[] {10, 30});
        //graph.output(input);

        //String simpleMlp = new ClassPathResource("model.h5").getFile().getPath();
        //MultiLayerNetwork model = KerasModelImport.importKerasSequentialModelAndWeights(simpleMlp);
        MultiLayerNetwork model = KerasModelImport.importKerasSequentialModelAndWeights("C:\\Users\\Patrick\\Documents\\GitHub\\KrisletLstmTrainerAndEvaluator\\Krislet_dl4j\\models\\model.h5");
        //System.out.println(model.getInput());
        System.out.println(model.summary());
        System.out.println("Example completed.");
    }
}
