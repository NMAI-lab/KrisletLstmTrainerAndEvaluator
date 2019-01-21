package KrisletDemo;

/**
 * Test import of DeepMoji application
 *
 * @author Max Pumperla
 */
public class Tester {

    public static void main(String[] args) {

        BehaviourModel model = new BehaviourModel();
        double ballDistance = Math.random() * 20;
        double ballDirection = Math.random() * 20;
        double goalDistance = Math.random() * 20;
        double goalDirection = Math.random() * 20;
        int action = model.getAction(ballDistance, ballDirection, goalDistance, goalDirection);
        // actions correspond to ['turn+','turn-', 'dash', 'kick']
        System.out.println(action);
    }
}
