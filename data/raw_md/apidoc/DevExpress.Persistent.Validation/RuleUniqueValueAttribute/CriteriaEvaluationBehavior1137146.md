---
uid: DevExpress.Persistent.Validation.RuleUniqueValueAttribute.CriteriaEvaluationBehavior
name: CriteriaEvaluationBehavior
type: Property
summary: Specifies whether to look for objects that are currently retrieved from the database, in addition to the objects in the database itself.
syntax:
  content: public CriteriaEvaluationBehavior CriteriaEvaluationBehavior { get; set; }
  parameters: []
  return:
    type: DevExpress.Persistent.Validation.CriteriaEvaluationBehavior
    description: A [](xref:DevExpress.Persistent.Validation.CriteriaEvaluationBehavior) enumeration value representing the behavior for searching for the required objects.
seealso: []
---
The following values are available:

* BeforeTransaction
    
    Only objects in the database will be considered.
* InTransaction
    
    Objects in the database and those that are currently retrieved from it will be considered.

By default, this property is set to **InTransaction**.

> [!NOTE]
> When defining the [](xref:DevExpress.Persistent.Validation.RuleUniqueValueAttribute) in code, the value for the **CriteriaEvaluationBehavior** property is passed as a named parameter. This means that you do not have to specify it. However, when specifying the parameter, use the following format: `CriteriaEvaluationBehavior = CriteriaEvaluationBehavior.InTransaction`.