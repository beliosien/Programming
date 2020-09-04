using System.Collections;
using System.Collections.Generic;
using UnityEngine;

// All the constants of the game
public static class GameConstants 
{
    // Tags
    public const string WALL = "Wall";
    public const string PLAYER = "Player";
    public const string ENEMY = "Enemy";
    public const string BOARD = "Board";

    // Movement
    public const float STEP_LENGTH = 0.2f;
    
}

// direction of the player 
public enum PlayerDirection 
{
    LEFT,
    RIGHT,
    UP ,
    DOWN,
    STAY
}
