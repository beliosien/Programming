using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class LivingEntity : MonoBehaviour, IDamageable
{
    public float startingHealth;
    protected float health;

    // Start is called before the first frame update
    protected virtual void Start()
    {
        health = startingHealth;
    }

    public void TakeDamage(float damage){
        print("ouch");
    }

    void Die(){
        print("dead");
    }
}
