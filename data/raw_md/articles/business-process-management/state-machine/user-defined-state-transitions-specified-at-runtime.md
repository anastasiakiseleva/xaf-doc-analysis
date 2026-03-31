---
uid: "113714"
seealso: []
title: User-Defined State Transitions Specified at Runtime
---
# User-Defined State Transitions Specified at Runtime

This topic describes how users can create and customize [State Machines](xref:113713) at runtime.

When the [State Machine Module](xref:113713) is added to an application, the **State Machine** navigation item is created automatically. This navigation item invokes a [List View](xref:112611) where you can create and customize persistent objects that define state machines.

State Machines are persisted using business objects (entities) that implement the **DevExpress.ExpressApp.StateMachine.IStateMachine** interface. If you are using XPO, the **DevExpress.ExpressApp.StateMachine.Xpo.XpoStateMachine** persistent class and its associated types are used automatically. If you use Entity Framework, you should manually add the following entities from the [Business Class Library](xref:112571) to your **DBContext**.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.Persistent.BaseImpl.EF.StateMachine;
// ...
public DbSet<StateMachine> StateMachines { get; set; }
public DbSet<StateMachineState> StateMachineStates { get; set; }
public DbSet<StateMachineTransition> StateMachineTransitions { get; set; }
public DbSet<StateMachineAppearance> StateMachineAppearances { get; set; }
```

***

To create a new state machine, use the **New** Action.

![StateMachine - RuntimeCreation1](~/images/statemachine-runtimecreation1116886.png)

When creating a state machine, specify its name, the target business class, and a property whose values represent the state of a business class instance. This can either be an [enumeration property](xref:113552) or a [reference property](xref:113572). Property values are used as state markers. Different states must use different marker values. You can now create states and transitions.

![StateMachine - RuntimeCreation2](~/images/statemachine-runtimecreation2116887.png)
> [!NOTE]
> To make a required business class available in the **Target Object Type** combo box, please add an [enumeration](xref:113552) or [reference](xref:113572) property (which will be used as a state marker) to this class.

When creating a state, specify its caption and corresponding value of the marker property. You can optionally specify criteria that an object must satisfy in order to obtain the current state. If the object does not satisfy the target object criteria, and a user tries to execute a transition to the state, the user is warned and the transition is canceled.

![StateMachine - RuntimeCreation3](~/images/statemachine-runtimecreation3116888.png)

Finally, specify transitions allowed for the current state and optionally, the appearance rules associated with the current state. The specified appearance rules will be in effect while an object is in its
+ current state.

![StateMachine - RuntimeCreation4](~/images/statemachine-runtimecreation4116902.png)

To control the visual order of state transitions, specify their **Index** property. Actions corresponding to state transitions are ordered according to their indices. To specify that a state transition should save the current object and to close the Detail View after execution, check the **Save and Close View** check box.

As a result, the **StateMachineController** will add the **ChangeStateAction** Action to Views that display objects of the type specified using the **Target Object Type** property.

![StateMachine - ShowActionsInToolBar](~/images/statemachine-showactionsintoolbar116890.png)

You can optionally check the **Expand Actions In Detail View** checkbox. In this instance, the target objects type's Detail Views will contain separate [Simple Actions](xref:112622) corresponding to available state transitions.

![StateMachine - ShowActionsInPanel](~/images/statemachine-showactionsinpanel116889.png)
> [!NOTE]
> Correct security permission configuration may be required when the State Machine module operates with data protected by the [Security System](xref:113366). _Read_ permissions should be granted to data required by State Machine, and _write_ permissions should be granted to data that will be modified, as the State Machine cannot bypass the security restrictions.