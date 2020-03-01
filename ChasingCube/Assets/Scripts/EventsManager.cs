using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Events;

/// <summary>
/// The event manager
/// </summary>
public static class EventsManager
{
    #region Fields

    // reduce speed event support
    static List<SlowerBehavior> reduceSpeedInvokers = new List<SlowerBehavior>();
    static List<UnityAction<CubeScript>> reduceSpeedListeners = new List<UnityAction<CubeScript>>();

    #endregion

    #region Methods

    /// <summary>
    /// Adds the invoker for the ReduceSpeedEvent
    /// </summary>
    /// <param name="invoker">invoker</param>
    public static void AddReduceSpeedInvoker(SlowerBehavior invoker)
    {
        reduceSpeedInvokers.Add(invoker);
        foreach (UnityAction<CubeScript> listener in reduceSpeedListeners)
        {
            invoker.AddReduceSpeedListener(listener);
        }
    }


    /// <summary>
    /// Adds the listener for the ReduceSpeedEvent
    /// </summary>
    /// <param name="listener">listener</param>
    public static void AddReduceSpeedListener(UnityAction<CubeScript> listener)
    {
        reduceSpeedListeners.Add(listener);
        foreach (SlowerBehavior invoker in reduceSpeedInvokers)
        {
            invoker.AddReduceSpeedListener(listener);
        }
    }

    #endregion
}
