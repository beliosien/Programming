using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class LivingEntity : MonoBehaviour, IDamageable
{
    public float startingHealth;
    protected float health;
    protected bool dead;

    // Start is called before the first frame update
    protected virtual void Start()
    {
        health = startingHealth;
    }
    
    ///<summary>
    /// Reduce the health by a damage passed as parameter.
    ///</summary>
    public void TakeDamage(float damage){
        health -= damage;
        if (health <= 0 && !dead){
            Die(); 
        }
    }

    ///<summary>
    /// Set the dead variable to true to indicate that the entity is dead.
    ///</summary>
    void Die(){
       dead = true;
    }
}
