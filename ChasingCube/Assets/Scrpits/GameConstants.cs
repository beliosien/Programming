using System.Collections;
using System.Collections.Generic;
using UnityEngine;

// All the constants of the game
public static class GameConstants 
{
    // Tags
    const string WALL = "Wall";
    const string PLAYER = "Player";
    const string ENEMY = "Enemy";
    const string BOARD = "Board";

    // Movement
    const float SPEED = 0.1f;
    
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
