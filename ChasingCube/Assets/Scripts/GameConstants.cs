
///<summary>
/// Game constants
///</summary>
public static class GameConstants
{

    public static float MAX_SPEED = 100.0f;
    public static float INCREASE_VALUE = 0.25f;
    public static float INITIAL_SPEED = 2.0f;
    public static float DAMAGE_POINT = 10.0f;
    public static float HEALTH = 10.0f;
    
    public static string HUNTER = "hunter";
    public static string HUNTED = "hunted";


    ///<summary>
    /// the type of cube in the game
    ///</summary>
    public enum CubeType
    {
        speedsterCube = 0,
        slowerCube = 1,
        tricksterCube = 2,
        jumperCube = 3
    }
} 