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
        target = GameObject.FindGameObjectWithTag(GameConstants.PLAYER).transform;
        targetRadius = target.GetComponent<CapsuleCollider>().radius;
        myRadius = GetComponent<CapsuleCollider>().radius;
        navMeshAgent = GetComponent<NavMeshAgent>();

    }

    // Update is called once per frame
    void Update()
    {
       Move();
    }

    ///<summary>
    /// Move the enemy toward the player.
    ///</summary>
    void Move(){
        Vector3 directionToTarget = new Vector3(target.position.x, 0, target.position.z);

        if (!dead){
            float distance = Vector3.Distance(transform.position, directionToTarget);

            if (distance - targetRadius - myRadius <= stopDistanceThreshold){
                    navMeshAgent.velocity = Vector3.zero;
            } else
            {
                navMeshAgent.SetDestination(directionToTarget);
            }
        }

    }

    private void OnTriggerEnter(Collider other) {
        if (other.gameObject.tag == GameConstants.BOMB){
            print("collision");
            TakeDamage(GameConstants.BOMB_DAMAGE);

            if (other.gameObject != null){
                Destroy(other.gameObject);
            }
        }
    }
}
