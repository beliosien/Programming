using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.AI;

public class Slower : Player
{

    GameObject[] enemiesObject;
    protected override void Start()
    {
        base.Start();
        enemiesObject = GameObject.FindGameObjectsWithTag("Enemy");
    }

    public override IEnumerator SuperPower()
    {
        Queue<float> originalSpeedQueue = new Queue<float>();

        foreach (GameObject gameObject in enemiesObject)
        {
            NavMeshAgent enemyNavMesh = gameObject.GetComponent<NavMeshAgent>();
            originalSpeedQueue.Enqueue(enemyNavMesh.speed);
            enemyNavMesh.speed = enemyNavMesh.speed * GameConstants.SLOWPERCENTAGE;
        }
        
        yield return new WaitForSeconds(superPowerDelay);

        foreach (GameObject gameObject in enemiesObject)
        {
            NavMeshAgent enemyNavMesh = gameObject.GetComponent<NavMeshAgent>();
            enemyNavMesh.speed =  originalSpeedQueue.Dequeue();
        }
    }
}
