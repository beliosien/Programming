using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.AI;

public class Trickster : Player
{
    public GameObject bombPrefab;

    enum TRICK_TYPE {
        REDUCE_SCALE,
        BOMB,
        STOP
    };

    TRICK_TYPE trick_type;
    int minRandomVal = 0;
    int maxRandomVal = 3;

    GameObject[] enemiesObjects;

    protected override void Start()
    {
        base.Start();
        enemiesObjects = GameObject.FindGameObjectsWithTag("Enemy");
    }

    public override IEnumerator SuperPower()
    {
        trick_type = (TRICK_TYPE) Random.Range(minRandomVal, maxRandomVal);
        
        switch (trick_type)
        {
            case TRICK_TYPE.REDUCE_SCALE:
                yield return ReduceScale();
                break;
            
            case TRICK_TYPE.BOMB:
                break;
            
            case TRICK_TYPE.STOP:
                yield return StopEnemies();
                break;
        }
    }

    IEnumerator ReduceScale(){

        foreach (GameObject gameObject in enemiesObjects)
        {
            gameObject.transform.localScale = Vector3.one * GameConstants.SCALE_REDUCE_PERCENTAGE;
        }
        
        yield return new WaitForSeconds(superPowerDelay);

        foreach (GameObject gameObject in enemiesObjects)
        {
            gameObject.transform.localScale = Vector3.one;
        }
    }

    void BomBEnemies(){

    }

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
