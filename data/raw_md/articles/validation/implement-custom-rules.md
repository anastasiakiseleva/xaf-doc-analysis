---
uid: "113051"
seealso:
- linkId: "113010"
title: Implement Custom Rules
---
# Implement Custom Rules

The **XAF** supplies a number of rules. You can use a corresponding rule attribute to apply them to business classes and their properties. To get the list of available rules and their attributes, refer to the [Validation Rules](xref:113008) topic. However, the supplied rules are universal may not work in every scenario. In these instances, you can implement a custom validation rule. This topic explains two approaches: implementing a typical XAF rule that is applied via a specific rule attribute, and implementing a rule that is automatically applied to a specified business class.

## Implement a Regular Validation Rule

To implement a new validation rule, inherit it from any XAF validation rule type listed in the table below. Some of these types are abstract and represent a base for rules. Use them as base classes to implement a custom rule. To modify the behavior of an existing XAF rule, inherit your rule directly from this particular rule type. Every rule should have the following auxiliary entities:

Rule Attribute
:   To create an instance of a rule of a particular type for a business class or a property, a rule attribute should be applied to this class or property. Each rule type has a specific attribute. Basically, an attribute establishes a set of parameters that are required to check the rule.  When implementing a custom rule, you should implement a custom attribute for it. For this purpose, you can inherit either from the [](xref:DevExpress.Persistent.Validation.RuleBaseAttribute), or from the attribute that corresponds to the rule you inherit from. In your attribute, you should, at a minimum, override the protected **RuleType** property, returning your rule type.

Rule Properties
:   Information on the rules to create in the application is saved to the [Application Model](xref:112580). Each validation rule exposes a [](xref:DevExpress.Persistent.Validation.RuleBaseProperties) class descendant via the [RuleBase.Properties](xref:DevExpress.Persistent.Validation.RuleBase.Properties) property. This descendant specifies the rule's properties exported to the corresponding **Validation** | **Rules** | **Rule** child node. When implementing a custom rule, you have the following options:
	1. If you need to extend the Properties class used by the rule's base rule, perform the following actions. First, declare a new interface derived from the interface implemented by the base Properties class. Declare the required additional properties in this interface. Second, declare the new Properties class by inheriting from the base Properties class. The new class must implement the newly declared interface. To make your rule, use the custom Properties class, override the **PropertiesType** property of the rule and the rule's attribute classes. In the overridden properties, return an instance of the descendant Properties class. Hide the base class' **Properties** property via the _new_ modifier. The property should have the type of the newly declared interface.
	2. If you are satisfied with the properties presented in the Properties type that is set for your rule's base rule, you do not have to override the **PropertiesType** properties.

The following table lists the available rule types, corresponding attributes and Properties types:

{|
|-

! Rule Type
! Rule Description
! Properties Type
! Attribute
|-

| [](xref:DevExpress.Persistent.Validation.RuleBase)
| Represents an abstract class implementing the [](xref:DevExpress.Persistent.Validation.IRule) interface.

Used as a base class for all rules.
| [](xref:DevExpress.Persistent.Validation.RuleBaseProperties)

Implements the [](xref:DevExpress.Persistent.Validation.IRuleBaseProperties) interface.
| -
|-

| **RuleCombinationOfPropertiesIsUnique**
| Represents the **RuleSearchObject** class descendant.

This rule demands that a particular properties' values combination is unique.
| [](xref:DevExpress.Persistent.Validation.RuleCombinationOfPropertiesIsUniqueProperties)

Derived from the **RuleSearchObjectProperties** class. Implements the **IRuleCombinationOfPropertiesIsUniqueProperties** interface.
| [](xref:DevExpress.Persistent.Validation.RuleCombinationOfPropertiesIsUniqueAttribute)

Derived from the **RuleBaseAttribute** class. Implements the **IRuleCombinationOfPropertiesIsUniqueProperties** interface.
|-

| **RuleCriteria**
| Represents the **RuleBase** class descendant.

 This rule demands that an object of a particular type satisfy a specified criteria.
| [](xref:DevExpress.Persistent.Validation.RuleCriteriaProperties)

Derived from the **RuleBaseProperties** class. Implements the **IRuleCriteriaProperties** interface.
| [](xref:DevExpress.Persistent.Validation.RuleCriteriaAttribute)

Derived from the **RuleBaseAttribute** class. Implements the **IRuleCriteriaProperties** interface.
|-

| **RuleFromBoolProperty**
| Represents the **RulePropertyValue\<TPropertyValue>** class descendant.

This rule demands that a Boolean type property should have a True value.
| [](xref:DevExpress.Persistent.Validation.RuleFromBoolPropertyProperties)

Derived from the **RulePropertyValueProperties** class. Implements the **IRuleFromBoolPropertyProperties** interface.
| [](xref:DevExpress.Persistent.Validation.RuleFromBoolPropertyAttribute)

Derived from the **RuleBaseAttribute** class. Implements the **IRuleFromBoolPropertyProperties** interface.
|-

| **RuleIsReferenced**
| Represents the **RuleSearchObject** class descendant.

 This rule demands that an object should be referenced in objects of a specified type.
| [](xref:DevExpress.Persistent.Validation.RuleIsReferencedProperties)

Derived from the **RuleSearchObjectProperties** class. Implements the **IRuleIsReferencedProperties** interface.
| [](xref:DevExpress.Persistent.Validation.RuleIsReferencedAttribute)

Derived from the **RuleBaseAttribute** class. Implements the **IRuleIsReferencedProperties** interface.
|-

| **RuleObjectExists**
| Represents the **RuleSearchObject** class descendant.

 This rule demands that an object of a particular type that satisfies a specified criteria, exists in the database.
| [](xref:DevExpress.Persistent.Validation.RuleObjectExistsProperties)

Derived from the **RuleSearchObjectProperties** class. Implements the **IRuleObjectExistsProperties** interface.
| [](xref:DevExpress.Persistent.Validation.RuleObjectExistsAttribute)

Derived from the **RuleBaseAttribute** class. Implements the **IRuleObjectExistsProperties** interface.
|-

| **RulePropertyValue**
| Represents an abstract class derived form the **RuleBase** class.

Used as a base class for the rules that check a specified property's value.
| [](xref:DevExpress.Persistent.Validation.RulePropertyValueProperties)

Derived from the **RuleBaseProperties** class. Implements the **IRulePropertyValueProperties** interface.
| -
|-

| **RulePropertyValue\<TPropertyValue>**
| Represents an abstract class derived from the **RulePropertyValue** class.

Used as a base class for the rules that checks a particular type of specified property's value.
| [](xref:DevExpress.Persistent.Validation.RulePropertyValueProperties)

Derived from the **RuleBaseProperties** class. Implements the **IRulePropertyValueProperties** interface.
| -
|-

| **RuleRange**
| Represents the **RulePropertyValue\<TPropertyValue>** class descendant.

This rule demands that a particular property's value should be within the specified value range.
| [](xref:DevExpress.Persistent.Validation.RuleRangeProperties)

Derived from the **RulePropertyValueProperties** class. Implements the **IRuleRangeProperties** interface.
| [](xref:DevExpress.Persistent.Validation.RuleRangeAttribute)

Derived from the **RuleBaseAttribute** class. Implements the **IRuleRangeProperties** interface.
|-

| **RuleRegularExpression**
| Represents the **RulePropertyValue\<TPropertyValue>** class descendant.

This rule demands that a particular property should match a specified pattern.
| [](xref:DevExpress.Persistent.Validation.RuleRegularExpressionProperties)

Derived from the **RulePropertyValueProperties** class. Implements the **IRuleRegularExpressionProperties** interface.
| [](xref:DevExpress.Persistent.Validation.RuleRegularExpressionAttribute)

Derived from the **RuleBaseAttribute** class. Implements the **IRuleRegularExpressionProperties** interface.
|-

| **RuleRequiredField**
| Represents the **RulePropertyValue\<TPropertyValue>** class descendant.

This rule demands that a particular property should have a value.
| [](xref:DevExpress.Persistent.Validation.RuleRequiredFieldProperties)

Derived from the **RulePropertyValueProperties** class. Implements the **IRuleRequiredFieldProperties** interface.
| [](xref:DevExpress.Persistent.Validation.RuleRequiredFieldAttribute)

Derived from the **RuleBaseAttribute** class. Implements the **IRuleRequiredFieldProperties** interface.
|-

| **RuleSearchObject**
| Represents an abstract class derived form the **RuleBase** class.

Used as a base class for the **RuleObjectExists**, **RuleUniqueValue** and **RuleIsReferenced** rules. This rule's checking algorithm is based on searching an object by a particular criteria.
| [](xref:DevExpress.Persistent.Validation.RuleSearchObjectProperties)

Derived from the **RuleBaseProperties** class. Implements the **IRuleSearchObjectProperties** interface.
| -
|-

| **RuleStringComparison**
| Represents the **RulePropertyValue\<TPropertyValue>** class descendant.

This rule demands that a value of a particular String type property should satisfy a specified condition.
| [](xref:DevExpress.Persistent.Validation.RuleStringComparisonProperties)

Derived from the **RulePropertyValueProperties** class. Implements the **IRuleStringComparisonProperties** interface.
| [](xref:DevExpress.Persistent.Validation.RuleStringComparisonAttribute)

Derived from the **RuleBaseAttribute** class. Implements the **IRuleStringComparisonProperties** interface.
|-

| **RuleUniqueValue**
| Represents the **RuleSearchObject** class descendant.

 This rule demands that a particular property's value should be unique.
| [](xref:DevExpress.Persistent.Validation.RuleUniqueValueProperties)

Derived from the **RuleSearchObjectProperties** class. Implements the **IRuleUniqueValueProperties** interface.
| [](xref:DevExpress.Persistent.Validation.RuleUniqueValueAttribute)

Derived from the **RuleBaseAttribute** class. Implements the **IRuleUniqueValueProperties** interface.
|-

| **RuleValueComparison**
| Represents the **RulePropertyValue\<TPropertyValue>** class descendant.

This rule demands that a particular property's value satisfy a specified condition.
| [](xref:DevExpress.Persistent.Validation.RuleValueComparisonProperties)

Derived from the **RulePropertyValueProperties** class. Implements the **IRuleValueComparisonProperties** interface.
| [](xref:DevExpress.Persistent.Validation.RuleValueComparisonAttribute)

Derived from the **RuleBaseAttribute** class. Implements the **IRuleValueComparisonProperties** interface.
|}

> [!NOTE]
> All the rules, Property types and attributes that are presented in the table above are declared in the DevExpress.Persistent.Base.v<:xx.x:>.dll assembly, in the _DevExpress.Persistent.Validation.RuleBase_ namespace.

The following code demonstrates the key members that you should have in your rule, Properties interface, Properties type and attribute:

# [C#](#tab/tabid-csharp)

```csharp
//Declare the new Properties interface
[GenerateMessageTemplatesModel("MyRule")]
public interface IRuleMyProperties : IRuleSearchObjectProperties {
    [Category("Data")]
    string AdditionalProperty { get; set; }
}
[DomainComponent] //Here the RuleSearchObjectProperties is used as a base class
public class MyRuleProperties : RuleSearchObjectProperties, IRuleMyProperties {
    private string additionalProperty;
    public string AdditionalProperty {
        get { return additionalProperty; }
        set { additionalProperty = value; }
    }
}
//Here the RuleSearchObject is used as a base class
public class MyRule : RuleSearchObject {
    //A custom rule must have at least two constructors
    //The default constructor
    public MyRule() : base() { }
    //A constructor which takes an IRuleBaseProperties-descendant interface type parameter
    public MyRule(IRuleSearchObjectProperties properties) : base(properties) { }
    protected override bool IsValidInternal(object target, out string errorMessageTemplate) {
        //Check whether the rule is satisfied
    }
    public override ReadOnlyCollection<string> UsedProperties {
        get {
            //Specify the properties that will be highlighted when the rule is broken
            //In ASP.NET Core Blazor, specify all affected properties before the first evaluation.
        }
    }
    //If you have a custom Properties type, return the Properties object
    //cast to the corresponding interface type
    protected new IRuleMyProperties Properties {
        get {
            return (IRuleMyProperties)base.Properties;
        }
    }
    //If you have a custom Properties type, return it here
    public override Type PropertiesType {
        get {
            return typeof(MyRuleProperties);
        }
    }
}
//Here an abstract RuleBaseAttribute class is used as a base class
public class MyRuleAttribute : RuleBaseAttribute {
    //Return the type of the rule for which you implement this attribute
    protected override Type RuleType {
        get { return typeof(MyRule); }
    }
    //If you have a custom Properties type, return it
    protected override Type PropertiesType {
        get {
            return typeof(MyRuleProperties);
        }
    }
    public MyRuleAttribute(string id, string targetContextIDs, string additionalProperty)
        : base(id, targetContextIDs) {
        Properties.AdditionalProperty = additionalProperty;
    }
    public MyRuleAttribute(string id, DefaultContexts targetContexts, string additionalProperty)
        : base(id, targetContexts) {
        Properties.AdditionalProperty = additionalProperty;
    }
    //If you have a custom Properties type, return the Properties object
    //cast to the corresponding interface type
    protected new IRuleMyProperties Properties {
        get { return (IRuleMyProperties)base.Properties; }
    }
    public string AdditionalProperty {
        get { return Properties.AdditionalProperty; }
    }
}
```
***

> [!NOTE]
> [!include[RuleBaseAttribute-Properties-declaration](~/templates/RuleBaseAttribute-Properties-declaration.md)]

When implementing a custom Properties type, the following attributes can be useful:

* **RulePropertiesRequired**
	
	Applied to a property of a Properties class. Indicates that the rule node's property that corresponds to this property cannot be empty.
* **RulePropertiesMemberOf**
	
	Applied to a Properties class' property, specifying the name of a business class property that takes part in the rule's logic. This attribute's parameter passes the name of the Properties class' property, specifying the type containing the property that uses this attribute. For instance:
	
	# [C#](#tab/tabid-csharp)
	
	```csharp
	[DomainComponent]
	public class MyRuleProperties : RuleSearchObjectProperties, IRuleMyProperties {
	    private Type someType;
	    public Type SomeType {
	        get { return someType; }
	        set { someType = value; }
	    }
	    private string property1Name;
	    [RulePropertiesMemberOf("SomeType ")]
	    public string Property1Name{
	        get { return property1Name; }
	        set { property1Name = value; }
	    }
	    private string property2Name;
	    [RulePropertiesMemberOf("SomeType ")]
	    public string Property2Name{
	        get { return property2Name; }
	        set { property2Name= value; }
	    }
	}
	```
	***
* **RulePropertiesIndex**
	
	Applied to properties of a Properties class to specify the order in which the corresponding properties will be shown in the Model Editor.

To register a custom validation rule, override a module's **Setup** method that takes an **ApplicationModulesManager** instance as a parameter. The following code snippet illustrates this.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Validation;
//...
public sealed partial class MyModule : ModuleBase {
    //...
    public override void Setup(ApplicationModulesManager moduleManager) {
        base.Setup(moduleManager);
        ValidationRulesRegistrator.RegisterRule(moduleManager, typeof(MyRule), typeof(IRuleMyProperties));
    }
}
```
***

To see an example of implementing a custom rule and its attributes and properties, refer to the **FeatureCenter** demo installed with **XAF** that have the **RuleStringLengthComparison**, **RuleStringLengthComparisonAttribute**, and  **RuleStringLengthComparisonProperties** implemented. This demo is in the _[!include[PathToFeatureCenter](~/templates/path-to-feature-center.md)]_ folder.

## Implement a Code Rule

With the Code Rule approach, you do not implement a custom attribute or apply it to business classes. The approach is useful when you need to apply a validation rule in code to a business class implemented in a referenced assembly without using the Model Editor. You can also use this approach to check objects using a highly tailored algorithm.

The main idea of the Code Rule approach is that you implement a custom rule, as described above, and decorate it with the [](xref:DevExpress.Persistent.Validation.CodeRuleAttribute). This approach differs from the approach described above to collect validation rules. Typically, information on validation rules is loaded into the Application Model based on the rule attributes applied to business classes. With this approach, information on validation rules is loaded into the Application Model based on validation rule classes decorated with the **CodeRule** attribute.

The rule's target class can be specified in the rule's declaration using one of the following techniques:

* The target type is specified as a generic parameter for the rule's base class:
	
	# [C#](#tab/tabid-csharp)
	
	```csharp
	[CodeRule]
	public class MyCodeRule : RuleBase<Contact> {
	   protected override bool IsValidInternal(
	      Contact target, out string errorMessageTemplate) {
	      //Check whether the rule is satisfied
	   }
	    public MyCodeRule() : base("", "Save") { }
	    public MyCodeRule(IRuleBaseProperties properties) : base(properties) { }
	}
	```
	***
* The target type is passed as a parameter of the base rule's constructor:
	
	# [C#](#tab/tabid-csharp)
	
	```csharp
	[CodeRule]
	public class MyCodeRule : RuleBase {
	   protected override bool IsValidInternal(
	      object target, out string errorMessageTemplate) {
	      //Check whether the rule is satisfied
	   }
	    public MyCodeRule() : base("", "Save", typeof(Contact)) { }
	    public MyCodeRule(IRuleBaseProperties properties) : base(properties) { }
	}
	```
	***

You can specify the rule's target properties (properties that XAF highlights in the UI when the rule is broken) in the overridden [IRule.UsedProperties](xref:DevExpress.Persistent.Validation.IRule.UsedProperties) property getter. In ASP.NET Core Blazor, the editors for the listed properties trigger the re-evaluation of the rule when they are changed. You should specify all the affected properties before the first evaluation because the subscription takes place when XAF creates the controls.

# [C#](#tab/tabid-csharp)

```csharp
using System.Collections.ObjectModel;
// ...
public override ReadOnlyCollection<string> UsedProperties {
    get {
        return new ReadOnlyCollection<string>(new List<string>() { "Amount" });
    }
}
```
***

To access the [](xref:DevExpress.ExpressApp.IObjectSpace) instance in the `RuleBase` descendant, use the [](xref:DevExpress.ExpressApp.IObjectSpaceLink) interface:

```csharp{4}
public class MyCodeRule : RuleBase<Contact> {
    protected override bool IsValidInternal(
        Contact target, out string errorMessageTemplate) {
        var os = ((IObjectSpaceLink)this).ObjectSpace;
```

Do not forget to register the rule by overriding a module's **Setup** method that takes an **ApplicationModulesManager** instance as a parameter.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Validation;
//...
public sealed partial class MyModule : ModuleBase {
    //...
    public override void Setup(ApplicationModulesManager moduleManager) {
        base.Setup(moduleManager);
        ValidationRulesRegistrator.RegisterRule(moduleManager, typeof(MyCodeRule), typeof(IRuleBaseProperties));
    }
}
```
***

[!include[<`CodeRule` attribute>](~/templates/main-demo-tip.md)]