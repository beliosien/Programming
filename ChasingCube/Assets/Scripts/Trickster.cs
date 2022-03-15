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
        //trick_type = (TRICK_TYPE) Random.Range(minRandomVal, maxRandomVal);
        trick_type = TRICK_TYPE.BOMB;
        
        switch (trick_type)
        {
            case TRICK_TYPE.REDUCE_SCALE:
                yield return ReduceScale();
                break;
            
            case TRICK_TYPE.BOMB:
                yield return BombEnemies();
                break;
            
            case TRICK_TYPE.STOP:
                yield return StopEnemies();
                break;
        }
    }

    ///<summary>
    ///Reduce temporarily the scale of the enemies on the field.
    ///</summary>
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
