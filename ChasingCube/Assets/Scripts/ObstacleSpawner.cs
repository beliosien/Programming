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

    // spawn support
    int minSpawnSecond;
    int maxSpawnSecond; 

    Vector3 spawnLocationMin;
    Vector3 spawnLocationMax;
    Timer spawnTimer;



    // Start is called before the first frame update
    void Start()
    {
        Instantiate(prefabObstacle);
        GameObject tempObstacle = Instantiate(prefabObstacle) as GameObject;
        BoxCollider collider = tempObstacle.GetComponent<BoxCollider>();
        float ballColliderHalfWidth = collider.size.x / 2;
        float ballColliderHalfHeight = collider.size.z / 2;
       spawnLocationMin = new Vector2(
            tempObstacle.transform.position.x - ballColliderHalfWidth,
            tempObstacle.transform.position.z - ballColliderHalfHeight);
        spawnLocationMax = new Vector2(
            tempObstacle.transform.position.x + ballColliderHalfWidth,
            tempObstacle.transform.position.z + ballColliderHalfHeight);
        Destroy(tempObstacle);
        minSpawnSecond = 1;
        maxSpawnSecond = 6;

        spawnTimer = gameObject.AddComponent<Timer>();
        spawnTimer.Duration = TimerDuration();
        spawnTimer.Run();
    }

    // Update is called once per frame
    void Update()
    {
        if (spawnTimer.Finished) 
        {
            SpawnObstacle();
            spawnTimer.Duration = TimerDuration();
            spawnTimer.Run();    
        }
    }


    ///<summary>
    /// Spawn a new obstacle at random 
    /// position
    ///</summary>
   public void SpawnObstacle()
    {
       Vector3 spawnPosition = new Vector3(Random.Range(0,26), Random.Range(0,26), Random.Range(0,26));
       Instantiate(prefabObstacle, spawnPosition, Quaternion.identity);
    }

    public float TimerDuration()
    {
        return Random.Range(minSpawnSecond,maxSpawnSecond);
    }
}
