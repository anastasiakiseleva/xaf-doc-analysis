---
uid: "112619"
seealso: []
title: 'How to: Create an Action Using the Action Attribute'
---
# How to: Create an Action Using the Action Attribute

This example demonstrates how to create an [Action](xref:112622) within a persistent class declaration (i.e., how to convert a persistent class method into a [](xref:DevExpress.ExpressApp.Actions.SimpleAction) or [](xref:DevExpress.ExpressApp.Actions.PopupWindowShowAction)).


## Important Notes on Using the Action Attribute

Actions created with the @DevExpress.Persistent.Base.ActionAttribute are not designed to operate in List Views without any selected objects. The attribute's [ActionAttribute.SelectionDependencyType](xref:DevExpress.Persistent.Base.ActionAttribute.SelectionDependencyType) parameter can be set either to `RequireSingleObject` or `RequireMultipleObjects` (see [](xref:DevExpress.Persistent.Base.MethodActionSelectionDependencyType)). To create an Action that does not require the selected object, add a [Controller](xref:112621) and implement an Action in it (see [](xref:402157) and [](xref:402158)).

@DevExpress.Persistent.Base.ActionAttribute is primarily used in simple scenarios when you execute logic based on data available within the business class context (for instance, modify class properties). @DevExpress.Persistent.Base.ActionAttribute is not suitable for any UI-related logic and complex user interactions. It is also not possible to access @DevExpress.ExpressApp.XafApplication, [Views](xref:112611), and other XAF UI-related entities within the business class code, because it violates the [separation of concerns](https://en.wikipedia.org/wiki/Separation_of_concerns) principle and is against the [MVC](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller) architecture (your data model should not be tied to the UI). To access @DevExpress.ExpressApp.XafApplication, [Views](xref:112611), and other UI-related entities, implement [Controllers](xref:112621) with [Actions](xref:112622).

## Create A Simple Action

Add a `Task` business class to your project.

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
[DefaultClassOptions,ImageName("BO_Task"),DefaultProperty(nameof(Subject))]
public class Task : BaseObject {
    public virtual string Subject { get; set; }
    public virtual bool IsCompleted { get; set; }
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp
[DefaultClassOptions, ImageName("BO_Task"), DefaultProperty(nameof(Subject))]
public class Task : BaseObject {
    public Task(Session session) : base(session) { }
    private string subject;
    public string Subject {
        get { return subject; }
        set { SetPropertyValue(nameof(Subject), ref subject, value); }
    }
    private bool isCompleted;
    public bool IsCompleted {
        get { return isCompleted; }
        set { SetPropertyValue(nameof(IsCompleted), ref isCompleted, value); }
    }
}
```

***

Implement an Action that changes the `IsCompleted` property to `true`. Add the following `Complete` method to the `Task` class and decorate it with the [](xref:DevExpress.Persistent.Base.ActionAttribute).

# [C#](#tab/tabid-csharp)

```csharp
[Action(Caption="Complete", TargetObjectsCriteria = "Not [IsCompleted]")]
public void Complete() {
    IsCompleted = true;
}
```

***

Such methods are automatically collected from business classes by the `ObjectMethodActionsViewController`. This controller creates the `Task.Complete` Action, that invokes the `Complete` method for each selected `Task`. Note the use of the [ActionAttribute.TargetObjectsCriteria](xref:DevExpress.Persistent.Base.ActionAttribute.TargetObjectsCriteria) parameter. The Action is disabled for `Tasks` that are already completed (the `IsCompleted` property is `true`). You can pass other parameters to customize the Action's look and behavior. 

The images below illustrate the **Complete** Action in the UI.

**ASP.NET Core Blazor**

![ActionAttributeExample_CompleteAction](~/images/actionattributeexample_completeaction117048_blazor.png)

**WinForms**

![ActionAttributeExample_CompleteAction](~/images/actionattributeexample_completeaction117048.png)

## Create an Action that Displays a Pop-up Dialog

Extend the `Task` class with two additional properties (`Deadline` and `Comments`) to demonstrate a more complex scenario.

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
using DevExpress.ExpressApp.Model;
// ...
public virtual DateTime? Deadline { get; set; }

[FieldSize(FieldSizeAttribute.Unlimited),ModelDefault("AllowEdit", "False")]
public virtual string Comments { get; set; }

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp
using DevExpress.ExpressApp.Model;
// ...
private DateTime? deadline;
public DateTime? Deadline {
    get { return deadline; }
    set { SetPropertyValue(nameof(Deadline), ref deadline, value); }
}
private string comments;
[Size(SizeAttribute.Unlimited), ModelDefault("AllowEdit", "False")]
public string Comments {
    get { return comments; }
    set { SetPropertyValue(nameof(Comments), ref comments, value); }
}
```

***

Implement an Action that postpones the `Deadline` by a specified number of days and updates the `Comments` text.  First, declare the following [non-persistent class](xref:116516) that holds parameters to be specified when a user postpones a `Task`.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.DC;
// ...
[DomainComponent]
public class PostponeParametersObject {
    public PostponeParametersObject() { PostponeForDays = 1; }
    public uint PostponeForDays { get; set; }
    [FieldSize(FieldSizeAttribute.Unlimited)]
    public string Comment { get; set; }
}
```

***

Then, add the following `Postpone` method to the `Task` class. This method takes a parameter of the `PostponeParametersObject` type and is decorated with the `Action` attribute.

# [C#](#tab/tabid-csharp)

```csharp
[Action(Caption = "Postpone",
    TargetObjectsCriteria = "[Deadline] Is Not Null And Not [IsCompleted]")]
public void Postpone(PostponeParametersObject parameters) {
    if (Deadline.HasValue && !IsCompleted && (parameters.PostponeForDays > 0)) {
        Deadline += TimeSpan.FromDays(parameters.PostponeForDays);
        Comments += String.Format("Postponed for {0} days, new deadline is {1:d}\r\n{2}\r\n",
        parameters.PostponeForDays, Deadline, parameters.Comment);
    }
}
```

***

As a result, the **Task.Postpone** Action, that accompanies the `Task` Views, is automatically created. This Action invokes a dialog with the **PostponeParametersObject** Detail View and executes the `Postpone` method after a user specifies the parameters and clicks **OK**. The following images illustrate this.

**ASP.NET Core Blazor**

![The Postpone Action ASP.NET Core Blazor](~/images/actioattributeexample_postponeactionblazor117049.png)

**WinForms**

![The Postpone Action WinForms](~/images/actioattributeexample_postponeactionwin117049.png)

> [!TIP]
> If it is necessary to reorder parameters displayed in a popup dialog, modify the layout of a parameter object's Detail View in the [Model Editor](xref:112582). In the example above, the appropriate Detail View node is **PostponeParametersObject_DetailView**. Refer to the following topic to learn more about layout customizations: [View Items Layout Customization](xref:112817).

### Access the current object instance

If you declare a `PostponeParametersObject` constructor that takes a parameter of type `Task`, the current `Task` instance is passed to this constructor when a user initiates the Action.

# [C#](#tab/tabid-csharp)

```csharp
[DomainComponent]
public class PostponeParametersObject {
    private Task task;
    public PostponeParametersObject(Task task) {
        PostponeForDays = 1;
        this.task = task;
    }
    // ...
}
```

***
