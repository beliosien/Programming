using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.AI;


[RequireComponent (typeof(NavMeshAgent))]
public class Enemy : LivingEntity
{
    NavMeshAgent navMeshAgent;
    Transform target;

    float targetRadius;
    float stopDistanceThreshold = .5f;

    float myRadius;

    // Start is called before the first frame update
    protected override void Start()
    {
        base.Start();
        target = GameObject.FindGameObjectWithTag("Player").transform;
        targetRadius = target.GetComponent<CapsuleCollider>().radius;
        myRadius = GetComponent<CapsuleCollider>().radius;
        navMeshAgent = GetComponent<NavMeshAgent>();

    }

    // Update is called once per frame
    void Update()
    {
       Move();
    }

    void Move(){
        Vector3 directionToTarget = new Vector3(target.position.x, 0, target.position.z);
        float distance = Vector3.Distance(transform.position, directionToTarget);

        if (distance - targetRadius - myRadius <= stopDistanceThreshold){
                navMeshAgent.velocity = Vector3.zero;
        } else
        {
            navMeshAgent.SetDestination(directionToTarget);
        }

    }
}
