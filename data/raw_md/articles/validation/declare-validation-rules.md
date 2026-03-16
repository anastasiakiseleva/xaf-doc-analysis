---
uid: "113251"
seealso:
- linkId: "113217"
title: Declare Validation Rules
owner: Ekaterina Kiseleva
---
# Declare Validation Rules

This topic describes two ways to declare and apply [rules](xref:113008) that validate business objects and their property values:

* [Apply Validation Rules in Code](#apply-validation-rules-in-code)  
  Use this solution if you want to modify sources of the required business classes. 
* [Apply Validation Rules in the Model Editor](#apply-validation-rules-in-the-model-editor)  
  Use this solution to declare a Validation Rule for a business class whose source code cannot be modified (e.g., a business class declared in a third-party module).

> [!Note]
> Before you implement one of these solutions, ensure that you added a [Validation Module](xref:113684) to a [module project](xref:118045).

## Requirements for Non-Persistent Objects

If you want to validate [non-persistent objects](xref:116516) in the Save or Delete Context, ensure that the following conditions are met.

1. The non-persistent class implements the @System.ComponentModel.INotifyPropertyChanged interface or is inherited from the `NonPersistentBaseObject` or `NonPersistentLiteObject` class.
2. The static @DevExpress.ExpressApp.NonPersistentObjectSpace.AutoSetModifiedOnObjectChangeByDefault field or @DevExpress.ExpressApp.NonPersistentObjectSpace.AutoSetModifiedOnObjectChange property is set to `true`.
3. You use the @DevExpress.ExpressApp.XafApplication.CreateObjectSpace(System.Type) method to create an Object Space. 
4. You call the @DevExpress.ExpressApp.IObjectSpace.CreateObject``1 or @DevExpress.ExpressApp.IObjectSpace.GetObject(System.Object) method to get a non-persistent object. 
5. If you want to use a validated value of a non-persistent object property, you handle the [BaseObjectSpace.ObjectSaving](xref:DevExpress.ExpressApp.BaseObjectSpace.ObjectSaving), [BaseObjectSpace.ObjectSaved](xref:DevExpress.ExpressApp.BaseObjectSpace.ObjectSaved), or [BaseObjectSpace.Committed](xref:DevExpress.ExpressApp.BaseObjectSpace.Committed) event. These events are raised after successful validation. Note that the [ActionBase.Executed](xref:DevExpress.ExpressApp.Actions.ActionBase.Executed) event is raised before validation occurs.

## Apply Validation Rules in Code

To apply a specific Rule to a class or a property, add an attribute with the same name as the required Rule. To see the full list of built-in attributes, refer to the following help topic: [Validation Rules](xref:113008). An attribute's parameters allow you to specify a Rule's properties. For example, the `ContextIDs` parameter allows you to specify a [Context](xref:113685) for a Rule.

You can apply Rule attributes only to _public_ members of a business class.

The code below applies the `RuleCriteria` Rule to the `Incident` persistent class and the `RuleRequiredField` Rule to the `Incident.Subject` property. Both Rules are checked when you save this object. They also check if the property values are `null`, because the `SkipNullOrEmptyValues` parameter of these Rules is set to `false` (for the second Rule, it is the default value).

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
using System.ComponentModel;
using DevExpress.Persistent.Validation;
//...
[DefaultClassOptions]
[DefaultProperty(nameof(Subject))]
[RuleCriteria("RuleCriteria for Incident", DefaultContexts.Save, 
    "AssignedTo is not null", SkipNullOrEmptyValues = false)]
public class Incident : BaseObject {
    [RuleRequiredField("RuleRequiredField for Incident.Subject", 
       DefaultContexts.Save)]
    public virtual string Subject { get; set; }
    public virtual Person AssignedTo { get; set; }
}

[DefaultClassOptions]
public class Person : BaseObject {
    public virtual string FirstName { get; set; }
    public virtual string LastName { get; set; }
    // ...
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp
using System.ComponentModel;
using DevExpress.Persistent.Validation;
//...
[DefaultClassOptions]
[DefaultProperty(nameof(Subject))]
[RuleCriteria("RuleCriteria for Incident", DefaultContexts.Save, 
    "AssignedTo is not null", SkipNullOrEmptyValues = false)]
public class Incident : BaseObject {
    public Incident(Session session) : base(session) { }
    private Person assignedTo;
    private string subject;
    [RuleRequiredField("RuleRequiredField for Incident.Subject", 
       DefaultContexts.Save)]
    public string Subject { 
        get { 
            return subject; 
        }
        set { 
            SetPropertyValue(nameof(Subject), ref subject, value);
        }
    }
    public Person AssignedTo {
        get {
            return assignedTo;
        }
        set {
            SetPropertyValue(nameof(AssignedTo), ref assignedTo, value);
        }
    }
}
```
***

To customize Validation Rules, use the [](xref:DevExpress.ExpressApp.Validation.PersistenceValidationController). Refer to its description to find an example of how to use this Controller.

If a value does not pass validation, an editor shows an error icon. The Validation Error pop-up dialog displays a brief description of each error.

In WinForms applications, a pop-up window shows the `RuleSetValidationResultItem_ByTarget` List View if a broken Validation Rule is detected. This List View details all broken Rules.
	
![Validation_Save_Win](~/images/validation_save_win116605.png)
	
You can double click a record to view detailed information on a broken Rule and validation results.

You can also specify custom text for Rule messages. To do this, set the Rule attribute's `messageTemplate` parameter in code or change the **Rules** | **Rule** node's `CustomMessageTemplate` property in the Model Editor.

## Apply Validation Rules in the Model Editor
You can use the [Model Editor](xref:112582) to declare a Validation Rule in the [Application Model](xref:112580). The following Application Model nodes define Contexts and Rules:

* [!include[Node_Action](~/templates/node_action111373.md)] 
	
	Specify the node's @DevExpress.ExpressApp.Validation.IModelActionValidationContexts.ValidationContexts property to use this Action as a Context with the specified ID.

* **Validation** | **Contexts** 
	
	Use this node to localize Context captions. These captions are displayed in Views that show Rules objects. These objects contain information on Rules and Contexts used in your application. You can make these objects available in your application for administrative purposes. To localize a Context, select the **Add…** | **ValidationContext** item in the context menu of the **Contexts** node, and specify the `ID` and `Caption` properties.

* **Validation** | **ErrorMessageTemplates**
	
	This node allows you to change the default message template for a Rule type. Error messages show the new text when a Rule of this type is broken. Note that the `CustomMessageTemplate` property of **Rules** | **Rule** nodes and a Rule attribute's `CustomMessageTemplate` parameter override this text.

* **Validation** | **Rules**
	
	This node contains Rules from this Module, and all referenced Modules, and allows you to define custom Rules. You can add a Rule (`RuleRequiredField`, `RuleRange`, and so on) from the corresponding **Add…** context menu item and specify the new Rule's properties. All Rules have a `ContextIDs` property. Set this property to an Action's `ValidationContexts` property value or a Context identifier. You can also use the [DefaultContexts.Save](xref:DevExpress.Persistent.Validation.DefaultContexts.Save) or [DefaultContexts.Delete](xref:DevExpress.Persistent.Validation.DefaultContexts.Delete) Context for Rules of any type.

Invoke the Model Editor for a project that references a Validation Module to find information on Rules applied in code. This information is also available in a module where Rules are applied. This allows an application administrator to add and edit Rules and Contexts in the Model Editor. Note that this user must have access to the Model Editor. The following image shows how the Model Editor shows the Rules defined in the [Apply Rule Attributes in Code](#apply-validation-rules-in-code) section.

![Validation_ModelEditor](~/images/validation_modeleditor115694.png)

## Soft Validation
You can define **Soft Validation Rules** - Rules that end users can ignore. Use Soft Validation to warn users that data is invalid, but allow them to commit changes anyway. Set the [IRuleBaseProperties.ResultType](xref:DevExpress.Persistent.Validation.IRuleBaseProperties.ResultType) property to **Warning** or **Information** to define an ignorable Rule in the Model Editor. To define this Rule in code, set the [RuleBaseAttribute.ResultType](xref:DevExpress.Persistent.Validation.RuleBaseAttribute.ResultType) parameter to **Warning** or **Information**. For more information on result types, refer to the following enumeration description: [](xref:DevExpress.Persistent.Validation.ValidationResultType).

> [!NOTE]
> * Populate the [IRule.UsedProperties](xref:DevExpress.Persistent.Validation.IRule.UsedProperties) collection with names of properties to be validated and highlighted in the UI if a _warning_ or _info_ Rule is broken.
> * Set the [ValidationModule.IgnoreWarningAndInformationRules](xref:DevExpress.ExpressApp.Validation.ValidationModule.IgnoreWarningAndInformationRules) property to `true` if you want to disable Soft Validation Rules so that a user is not notified if these Rules are broken.  

The **Validation** | **Soft Validation** section of the **FeatureCenter** demo demonstrates how to implement and use **Soft Validation**. [!include[FeatureCenterLocationNote](~/templates/featurecenterlocationnote111102.md)]

## Define a Custom Rule Source
To create a custom Validation Rule Source, define a class that implements the [](xref:DevExpress.Persistent.Validation.IRuleSource) interface. The interface's [IRuleSource.CreateRules](xref:DevExpress.Persistent.Validation.IRuleSource.CreateRules) method allows you to implement custom logic to instantiate Validation Rules.

Refer to the following interface description to see how to implement a custom Validation Rule Source: [](xref:DevExpress.Persistent.Validation.IRuleSource).
