using System.Collections;
using System.Collections.Generic;
using UnityEngine;

// class that control our snake
public class PlayerController : MonoBehaviour
{
    [HideInInspector]
    public PlayerDirection direction;

    [HideInInspector]
    public float step_length = 0.2f;

    [HideInInspector]
    public float mouvement_frequency = 0.1f;
    private float counter;
    private bool move;

    [SerializeField]
    private GameObject tailPrefab;
    private List<Vector3> delta_position;
    private List<Rigidbody> nodes;

    private Rigidbody main_Body;
    private Rigidbody head_Body;
    private Transform tr;

    private bool create_Node_At_Tail;

    void Awake() 
    {
        tr =  transform;
        main_Body = GetComponent<Rigidbody>();

        InitSnakeNodes();
        InitPlayer();

        delta_position = new List<Vector3> {
            new Vector3(-step_length, 0.0f),  // LEFT
            new Vector3(0.0f, step_length),   // UP
            new Vector3(step_length, 0.0f),   // RIGHT
            new Vector3(0.0f, -step_length)    // DOWN
        };
    }

    // Update is called once per frame
    void Update()
    {
        CheckMouvementFrequency();
    }

    void FixedUpdate() 
    {
        if (move)
        {
            move  = false;
            Move();
        }
        
    }

    void InitSnakeNodes()
    {
        nodes = new List<Rigidbody>();

        nodes.Add(tr.GetChild(0).GetComponent<Rigidbody>());
        nodes.Add(tr.GetChild(1).GetComponent<Rigidbody>());
        nodes.Add(tr.GetChild(2).GetComponent<Rigidbody>());

        head_Body = nodes[0];
    }

    void SetDirectionRandom()
    {
        int dirRandom = Random.Range(0, (int)PlayerDirection.COUNT);
        direction = (PlayerDirection)dirRandom;
    }

    void InitPlayer()
    {
        SetDirectionRandom();
        switch (direction)
        {
            case PlayerDirection.RIGHT:
                nodes[1].position = nodes[0].position - new Vector3(Metric.NODE, 0.0f, 0.0f);
                nodes[2].position = nodes[0].position - new Vector3(Metric.NODE * 2, 0.0f, 0.0f);
                break;

            case PlayerDirection.LEFT:
                nodes[1].position = nodes[0].position + new Vector3(Metric.NODE, 0.0f, 0.0f);
                nodes[2].position = nodes[0].position + new Vector3(Metric.NODE * 2, 0.0f, 0.0f);
                break;

            case PlayerDirection.UP:
                nodes[1].position = nodes[0].position - new Vector3(0.0f, Metric.NODE, 0.0f);
                nodes[2].position = nodes[0].position - new Vector3(0.0f, Metric.NODE * 2, 0.0f);
                break;

            case PlayerDirection.DOWN:
                nodes[1].position = nodes[0].position + new Vector3(0.0f, Metric.NODE, 0.0f);
                nodes[2].position = nodes[0].position + new Vector3(0.0f, Metric.NODE * 2, 0.0f);
                break;
        }
    }

    void Move()
    {
        Vector3 dPosition = delta_position[(int)direction];
        Vector3 parentPos = head_Body.position;
        Vector3 prevPosition;

        main_Body.position = main_Body.position + dPosition;
        head_Body.position = head_Body.position + dPosition;

        for (int i = 1; i < nodes.Count; i++)
        {
            prevPosition = nodes[i].position;
            nodes[i].position = parentPos;
            parentPos = prevPosition;   
        }

        if (create_Node_At_Tail)
        {
            create_Node_At_Tail = false;
            GameObject newNode = Instantiate(tailPrefab, nodes[nodes.Count - 1].position, Quaternion.identity);
            newNode.transform.SetParent(transform, true);
            nodes.Add(newNode.GetComponent<Rigidbody>());
        }
    }

    void CheckMouvementFrequency()
    {
        counter += Time.deltaTime;
        if (counter >= mouvement_frequency)
        {
            counter = 0.0f;
            move = true;
        }
    }

    public void SetInputDirection(PlayerDirection dir)
    {
        if (dir == PlayerDirection.UP && direction == PlayerDirection.DOWN || 
            dir == PlayerDirection.DOWN && direction == PlayerDirection.UP ||
            dir == PlayerDirection.RIGHT && direction == PlayerDirection.LEFT || 
            dir == PlayerDirection.LEFT && direction == PlayerDirection.RIGHT) 
            {
                return;
            }

        direction = dir;
        ForceMove();
    }


    void ForceMove()
    {
        counter = 0;
        move = false;
        Move();
    }

    void OnTriggerEnter(Collider other) 
    {
        if (other.tag == Tags.FRUIT)
        {
            other.gameObject.SetActive(false);
            create_Node_At_Tail = true;
            GamePlayController.instance.IncreaseScore();
            AudioManager.instance.Play_PickUpSound();
        }

        if (other.tag == Tags.WALL || other.tag == Tags.BOMB || other.tag == Tags.TAIL)
        {
            Time.timeScale = 0f;
            AudioManager.instance.Play_DeadSound();
        }
        
    }
}
