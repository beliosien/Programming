
///<summary>
/// Game constants
///</summary>
public static class GameConstants
{

    ///<summary>
    /// the constant of the game
    ///</summary>
    public static float MAX_SPEED = 100.0f;
    public static float INCREASE_VALUE = 0.25f;
    public static float INITIAL_SPEED = 2.0f;
    public static float DAMAGE_POINT = 10.0f;
    public static float FACTOR_SPEED_REDUCE = 1.5f;
    public static float HEALTH = 10.0f;
    public static int DURATION = 5;

    ///<summary>
    /// the minimal distance between cube 
    ///</summary>
    public static float MINDIST = 1.02f;
    
    ///<summary>
    /// the tags of the game 
    ///</summary>
    public static string HUNTER = "hunter";
    public static string HUNTED = "hunted";

    ///<summary>
    /// the different names of the cube 
    ///</summary>
    public const string slowerCube ="slowerCube";
    public const string speedsterCube = "speedSterCube";

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