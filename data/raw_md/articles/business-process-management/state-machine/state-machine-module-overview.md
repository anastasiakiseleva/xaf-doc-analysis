---
uid: "113713"
seealso:
- linkId: "113714"
- linkId: "113715"
title: State Machine Module Overview
owner: Ekaterina Kiseleva
---
# State Machine Module Overview

Business objects often have an associated state specified by their property values (for example, a `Task` object has a status that can be _`NotStarted`_, _`InProgress`_, and so on.). While this state can easily be changed by modifying corresponding property values, managing state transitions in a uniform way is not that simple. This is why XAF ships with the State Machine module, which greatly simplifies state transition management.

## State Machine Capabilities
The module creates a set of [Actions](xref:112622) that correspond to state transitions and  display them in corresponding Views.

![StateMachine - ShowActionsInToolBar](~/images/statemachine-showactionsintoolbar116890.png)![StateMachine - ShowActionsInPanel](~/images/statemachine-showactionsinpanel116889.png)

With the State Machine, you can:

* define a set of states and corresponding transitions, and associate them with a business class. You can do this [in code](xref:113715) or [at runtime](xref:113714), as the State Machine module comes with predefined Views for state and transition management. The property whose values specify different object states can be either an enumeration-typed property or a reference property;
* define [Conditional Appearance](xref:113286) rules and associate them with particular states. This can also be done both in code and at runtime.

> [!IMPORTANT]
> [!include[StateMachine_Note](~/templates/statemachine_note111211.md)]

> [!NOTE]
> In the [DataView](xref:118452), [ServerView, InstantFeedback, and InstantFeedbackView](xref:118450) data access modes, **State Machine** requests selected objects from the database each time the selection is changed.

## Add the State Machine Module

To add the State Machine module to an ASP.NET Core Blazor or WinForms existing application, install the `DevExpress.ExpressApp.StateMachine` NuGet package and [register](xref:118047) the State Machine module in a platform-agnostic module (_MySolution.Module_):

# [C#](#tab/tabid-csharp)

```csharp
public sealed class MySolutionModule : ModuleBase {
    //...
    public MySolutionModule() {
        InitializeComponent();
        this.RequiredModuleTypes.Add(typeof(DevExpress.ExpressApp.StateMachine.StateMachineModule));
    }
}
```

***

> [!NOTE]
> [!include[ExtraModulesNote](~/templates/extramodulesnote11181.md)]
> * [!include[<@DevExpress.ExpressApp.ApplicationBuilder.StateMachineApplicationBuilderExtensions.AddStateMachine``1(DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{``0},System.Action{DevExpress.ExpressApp.StateMachine.StateMachineOptions})>,<ASP.NET Core Blazor/WinForms>](~/templates/ExtraModulesNote_ApplicationBuilder.md)]