using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class GamePlayController : MonoBehaviour
{
    public static GamePlayController instance;
    public GameObject fruit_PickUp, bomb_PickUp;
    private float min_X = -4.25f, max_X = 4.25f;
    private float min_Y = -2.26f, max_Y = 2.26f;
    private float z_Pos = 5.8f;

    private Text score_Text;
    private int scoreCount;
 
    // Start is called before the first frame update
    void Awake()
    {
        MakeInstance();
    }

    void Start() 
    {
        score_Text = GameObject.Find("Score").GetComponent<Text>();

        Invoke("StartSpawning",0.5f);
    }

    void MakeInstance()
    {
        if (instance == null)
        {
            instance = this;
        }
    }

    void StartSpawning()
    {
        StartCoroutine(SpawnPickUps());
    }

    public void CancelSpawing()
    {
        CancelInvoke("StartSpawning");
    }

    IEnumerator SpawnPickUps()
    {
        yield return new WaitForSeconds(Random.Range(1f, 1.5f));
        if (Random.Range(1,10) >= 2)
        {
            Instantiate(fruit_PickUp, new Vector3(Random.Range(min_X,max_X), Random.Range(min_Y, max_Y), z_Pos), Quaternion.identity);
        } else
        {
            Instantiate(bomb_PickUp, new Vector3(Random.Range(min_X,max_X), Random.Range(min_Y, max_Y), z_Pos), Quaternion.identity);
        }

        Invoke("StartSpawning",0);
    }

    public void IncreaseScore()
    {
        scoreCount++;
        score_Text.text = "Score: " + scoreCount;
    }
}
