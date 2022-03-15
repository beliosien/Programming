using System.Collections;
using System.Collections.Generic;
using UnityEngine;


[RequireComponent (typeof(Rigidbody))]
public class PlayerController : MonoBehaviour
{
    new Rigidbody rigidbody;
    Vector3 velocity;


    // Start is called before the first frame update
    void Start()
    {
        rigidbody = GetComponent<Rigidbody>();
    }

    public void Move(Vector3 _velocity){
        velocity = _velocity;

    }

    private void FixedUpdate() {
        rigidbody.MovePosition(rigidbody.position + velocity * Time.fixedDeltaTime);
    }
}
