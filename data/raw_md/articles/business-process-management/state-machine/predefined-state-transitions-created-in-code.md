---
uid: "113715"
seealso: []
title: Predefined State Transitions Created in Code
owner: Ekaterina Kiseleva
---
# Predefined State Transitions Created in Code

This topic describes how to create a predefined [State Machine](xref:113713) in code. A predefined State Machine cannot be changed by users. For information how to define a state machine at runtime, refer to the [User-Defined State Transitions Specified at Runtime](xref:113714) topic instead.

> [!IMPORTANT]
> [!include[StateMachine_Note](~/templates/statemachine_note111211.md)]

> [!NOTE]
> To see this example in action, refer to the **State Machine** section of the **Feature Center** demo located in the _[!include[PathToFeatureCenter](~/templates/path-to-feature-center.md)]_ folder by default, or refer to the [Feature Center demo online](https://demos.devexpress.com/XAF/FeatureCenter/XpoStateMachine_ListView/).

The following code defines a simple **Task** business class, which can have different states such as **not started**, **in progress**, **completed**, etc.

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl.EF;
using System.ComponentModel.DataAnnotations;
//...
public enum TaskStatus { Draft, NotStarted, InProgress, Paused, Completed, Dropped }

[DefaultClassOptions,ImageName("BO_Task")]
public class Task : BaseObject {
    public virtual string Subject { get; set; }
    public virtual TaskStatus Status { get; set; }
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl;
using DevExpress.Xpo;
//...
public enum TaskStatus { Draft, NotStarted, InProgress, Paused, Completed, Dropped }

[DefaultClassOptions, ImageName("BO_Task")]
public class Task : BaseObject {
    public Task(Session session) : base(session) { }
    public string Subject {
        get { return GetPropertyValue<string>(nameof(Subject)); }
        set { SetPropertyValue<string>(nameof(Subject), value); }
    }
    public TaskStatus Status {
        get { return GetPropertyValue<TaskStatus>(nameof(Status)); }
        set { SetPropertyValue<TaskStatus>(nameof(Status), value); }
    }
}
```
***

To create a state machine for this class, perform the following steps.

1. Declare a **StateMachine\<T>** class descendant with the generic type parameter specifying the target business class. Override the **Name** property to specify a textual description for a state machine.
	
	# [C#](#tab/tabid-csharp)
	
	```csharp
	using DevExpress.ExpressApp.StateMachine.NonPersistent;
	//...
	public class TaskStatusStateMachine : StateMachine<Task> {
	    public override string Name { 
	        get { return "Change status to"; } 
	    }
	}
	```
	***
2. Decide which business class property should be used as a **state property**. To function, a state machine must be able to distinguish between object states. This is why you need to specify a property whose values will represent different object states. This can be either an _enumeration-typed property_ or a _reference property_. In this example, the **Status** property is a perfect candidate. Thus, it is used as a **state property**, and consequently, its values will be used as **state markers**. Note that different states must use different marker objects. To specify a **state property**, override the **StatePropertyName** property.
	
	# [C#](#tab/tabid-csharp)
	
	```csharp
	public class TaskStatusStateMachine : StateMachine<Task> {
	    //...
	    public override string StatePropertyName { 
	        get { return "Status"; }
	    }
	}
	```
	***
3. Declare a set of allowed states and transitions between them. States are **State** class instances and transitions are **Transition** class instances. A state belongs to a state machine and has an associated caption and a marker. Each state has a collection of allowed transitions that specify possible target states. In this example, it should not be possible for a task to become **completed** until it is **in progress**, so the **in progress** state should not contain a **completed** transition.
	
	# [C#](#tab/tabid-csharp)
	
	```csharp
	using DevExpress.ExpressApp.StateMachine;
	//...
	public class TaskStatusStateMachine : StateMachine<Task> {
	    //...
	    private IState startState;
	    public TaskStatusStateMachine(IObjectSpace objectSpace) : base(objectSpace) {
	        startState = new State(this, TaskStatus.Draft);
	
	        IState notStartedState = new State(this, "Not Started", TaskStatus.NotStarted);
	        IState inProgressState = new State(this, "In Progress", TaskStatus.InProgress);
	        IState pausedState = new State(this, TaskStatus.Paused);
	        IState completedState = new State(this, TaskStatus.Completed);
	        IState droppedState = new State(this, TaskStatus.Dropped);
	
	        startState.Transitions.Add(new Transition(notStartedState));
	        notStartedState.Transitions.Add(new Transition(startState));
	        notStartedState.Transitions.Add(new Transition(inProgressState));            
	        inProgressState.Transitions.Add(new Transition(pausedState));
	        inProgressState.Transitions.Add(new Transition(completedState));
	        inProgressState.Transitions.Add(new Transition(droppedState));
	        pausedState.Transitions.Add(new Transition(inProgressState));
	        droppedState.Transitions.Add(new Transition(notStartedState));
	
	        States.Add(startState);
	        States.Add(notStartedState);
	        States.Add(inProgressState);
	        States.Add(pausedState);
	        States.Add(completedState);
	        States.Add(droppedState);
	    }
	    public override IState StartState { 
	        get { return startState; } 
	    }
	}
	```
	***
	
	After you have defined states, transitions, and appearance rules in a state machine constructor, add them to the machine's **States** collection. Override the **StartState** property to specify the initial state for newly created objects.
4. A state machine can optionally have [Conditional Appearance](xref:113286) rules associated with its states. These rules are represented by **StateAppearance** instances.
	
	# [C#](#tab/tabid-csharp)
	
	```csharp
	public class TaskStatusStateMachine : StateMachine<Task> {
	    //...
	    public TaskStatusStateMachine(IObjectSpace objectSpace) : base(objectSpace) {
	        //...        
	        StateAppearance inProgressAppearance = new StateAppearance(inProgressState);
	        inProgressAppearance.TargetItems = "Subject";
	        inProgressAppearance.Enabled = false;
	        StateAppearance completedAppearance = new StateAppearance(completedState);
	        completedAppearance.TargetItems = "Subject";
	        completedAppearance.Enabled = false;
	        StateAppearance pausedAppearance = new StateAppearance(pausedState);
	        pausedAppearance.TargetItems = "*";
	        pausedAppearance.BackColor = System.Drawing.Color.Yellow;
	    }
	}
	```
	***
5. Implement the **IStateMachineProvider** interface in the target business class. The interface's only member - **GetStateMachines** method - returns a list of all state machines available for the business class.
	
	# [C# (EF Core)](#tab/tabid-csharp-ef)

	```csharp
	using System.Collections.Generic;
	using DevExpress.ExpressApp.EFCore;
	using DevExpress.ExpressApp.StateMachine;
	using DevExpress.ExpressApp.EFCore;
	//...
	public class Task : BaseObject, IStateMachineProvider {
		//...
		public IList<IStateMachine> GetStateMachines() {
			List<IStateMachine> result = new List<IStateMachine>();
			result.Add(new TaskStatusStateMachine(EFCoreObjectSpace.FindObjectSpaceByObject(this)));
			return result;
		}
	}

	// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
	```

	# [C# (XPO)](#tab/tabid-csharp-xpo)
	
	```csharp
	using System.Collections.Generic;
	//...
	public class Task : BaseObject, IStateMachineProvider {
	    //...
	    public IList<IStateMachine> GetStateMachines() {
	        List<IStateMachine> result = new List<IStateMachine>();
	        result.Add(new TaskStatusStateMachine(XPObjectSpace.FindObjectSpaceByObject(this)));
	        return result;
	    }
	}
	```
	***

The State Machine module will display the **ChangeStateAction** Action in **Task** Views. The Action is provided by the **StateMachineController**.

![StateMachine - ShowActionsInToolBar](~/images/statemachine-showactionsintoolbar116890.png)

> [!NOTE]
> The **StateMachineController** is not designed to execute additional logic using its **TransitionExecuting** and **TransitionExecuted** events. Instead, place your custom code in the setter of the desired business class property.

You can optionally implement the **IStateMachineUISettings** interface and set its **ExpandActionsInDetailView** property to **true**.

# [C#](#tab/tabid-csharp)

```csharp{1,3-5}
public class TaskStatusStateMachine : StateMachine<Task>, IStateMachineUISettings {
    //...
    public bool ExpandActionsInDetailView {
        get { return true; }
    }
}
```
***

In this instance, the target business class Detail Views will contain separate [Simple Actions](xref:112622) corresponding to available state transitions.

![StateMachine - ShowActionsInPanel](~/images/statemachine-showactionsinpanel116889.png)
