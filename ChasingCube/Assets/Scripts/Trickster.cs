using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.AI;

public class Trickster : Player
{
    public GameObject bombPrefab;

    enum TRICK_TYPE {
        BOMB,
        STOP
    };

    TRICK_TYPE trick_type;
    int minRandomVal = 0;
    int maxRandomVal = 2;

    GameObject[] enemiesObjects;

    protected override void Start()
    {
        base.Start();
        enemiesObjects = GameObject.FindGameObjectsWithTag(GameConstants.ENEMY);
    }

    public override IEnumerator SuperPower()
    {
        trick_type = (TRICK_TYPE) Random.Range(minRandomVal, maxRandomVal);
        
        switch (trick_type)
        {
            case TRICK_TYPE.BOMB:
                yield return BombEnemies();
                break;
            
            case TRICK_TYPE.STOP:
                yield return StopEnemies();
                break;
        }
    }


    ///<summary>
    /// Threw bomb at enemies on the field.
    ///</summary>
    IEnumerator BombEnemies(){
        Vector3 position = new Vector3(transform.position.x, bombPrefab.transform.position.y, transform.position.z);
        GameObject newBomb = Instantiate(bombPrefab, position, Quaternion.identity) as GameObject;
        
        // giving force to the bomb to give the throwing effect
       
        yield return new WaitForSeconds(superPowerDelay);

        if (newBomb != null){
            Destroy(newBomb);
        }
    }

    ///<summary>
    ///Stop enemies movements temporarily.
    ///</summary>
    IEnumerator StopEnemies(){
        Queue<Vector3> originalVelocityQueue = new Queue<Vector3>();

        foreach (GameObject gameObject in enemiesObjects)
        {
            NavMeshAgent enemyNavMesh = gameObject.GetComponent<NavMeshAgent>();
            originalVelocityQueue.Enqueue(enemyNavMesh.velocity);
            enemyNavMesh.velocity = Vector3.zero;
        }
        
        yield return new WaitForSeconds(superPowerDelay);

        foreach (GameObject gameObject in enemiesObjects)
        {
            NavMeshAgent enemyNavMesh = gameObject.GetComponent<NavMeshAgent>();
            enemyNavMesh.velocity =  originalVelocityQueue.Dequeue();
        }
    }

}
