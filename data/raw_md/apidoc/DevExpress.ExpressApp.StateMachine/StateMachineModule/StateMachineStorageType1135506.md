---
uid: DevExpress.ExpressApp.StateMachine.StateMachineModule.StateMachineStorageType
name: StateMachineStorageType
type: Property
summary: Specifies a persistent type used to store state machines in the database.
syntax:
  content: public Type StateMachineStorageType { get; set; }
  parameters: []
  return:
    type: System.Type
    description: A persistent type used to store state machines in the database.
seealso: []
---
<!--TODO How to change the property's value without Application Designer? -->

The specified type should implement the **IStateMachine** interface. XAF provides you with two predefined types:

* `DevExpress.ExpressApp.StateMachine.Xpo.XpoStateMachine` (XPO)
* `DevExpress.Persistent.BaseImpl.EF.StateMachine.StateMachine` (EF) 

Set the `StateMachineStorageType` property to the corresponding type after you add the State Machine Module to your application.