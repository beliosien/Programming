using System.Collections;
using System.Collections.Generic;
using UnityEngine;

///<summary>
// This Class spawn the obstacle 
// on the scene randomly
///</summary>
public class ObstacleSpawner : MonoBehaviour
{
    [SerializeField]
    GameObject prefabObstacle;

    // spawn control
	Timer spawnTimer;
    const float SpawnDelay = 0.3f;
    const int MaxNumObstacles = 5;

    // spawn location support
    Vector3 location = Vector3.zero;
	float minSpawnX;
	float maxSpawnX;
	float minSpawnZ;
	float maxSpawnZ;


    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
