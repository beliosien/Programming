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
    float attackDistanceThreshold = .5f;

    float myRadius;

    // Start is called before the first frame update
    protected override void Start()
    {
        base.Start();
        target = GameObject.FindGameObjectWithTag(GameConstants.PLAYER).transform;
        targetRadius = target.GetComponent<CapsuleCollider>().radius;
        myRadius = GetComponent<CapsuleCollider>().radius;
        navMeshAgent = GetComponent<NavMeshAgent>();

        StartCoroutine(Move());

    }

    // Update is called once per frame
    void Update()
    {
    }

    ///<summary>
    /// Move the enemy toward the player.
    ///</summary>
    IEnumerator Move(){
        float refresh_rate = .25f;

        while(target != null){
            Vector3 directionToTarget = (target.position - transform.position).normalized;
            Vector3 targetPosition = target.position - directionToTarget * (myRadius + targetRadius + attackDistanceThreshold/2f);

            if (!dead){
                navMeshAgent.SetDestination(targetPosition);
            }

            yield return new WaitForSeconds(refresh_rate);
        }

    }

    ///<summary>
    /// Attack the player when in certain range
    ///</summary>
    void Attack(){

    }

    private void OnTriggerEnter(Collider other) {
        if (other.gameObject.tag == GameConstants.BOMB){
            TakeDamage(GameConstants.BOMB_DAMAGE);

            if (other.gameObject != null){
                Destroy(other.gameObject);
            }
        }
    }
}
