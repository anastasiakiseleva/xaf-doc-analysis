---
uid: DevExpress.Persistent.Validation.IRuleSource
name: IRuleSource
type: Interface
summary: Declares members that custom [Validation Rule](xref:113008) Sources implement.
syntax:
  content: public interface IRuleSource
seealso:
- linkId: DevExpress.Persistent.Validation.IRuleSource._members
  altText: IRuleSource Members
- linkId: "113251"
---
Implement the **IRuleSource** interface in your business class to create a custom Validation Rule Source. Custom Validation Rule Sources allow you to store Validation Rules in the database. We recommend that you use this technique if you need to frequently customize Validation Rules in a deployed application, but you cannot redeploy the application or customize its [Application Model](xref:112580).

> [!NOTE]
>
> Persistent validation rules are in action only if the application's database has been created and initialized. In debug mode, a new XAF application creates its database on the first login attempt (when a user clicks the _Log In_ button for the first time). For these reasons, if you define a persistent validation rule that affects the login form, this rule will not work until you complete the login process at least once. 

Refer to the following help topic for information on other techniques to declare Validation Rules: [Declare Validation Rules](xref:113251).

The **IRuleSource** interface declares the following members:

[IRuleSource.Name](xref:DevExpress.Persistent.Validation.IRuleSource.Name) property 
:   Returns the unique name of the custom Validation Rule Source. 
[IRuleSource.CreateRules](xref:DevExpress.Persistent.Validation.IRuleSource.CreateRules) method
:   Instantiates custom Validation Rules.

The Validation Module automatically collects persistent Validation Rule Sources and Rules when you start an application. Persistent Validation Rule Sources and Rules are persistent classes that implement the @DevExpress.Persistent.Validation.IRuleSource and @DevExpress.Persistent.Validation.IRule interfaces accordingly. Built-in Rule Sources query the database each time before validation occurs. Use the @DevExpress.ExpressApp.Validation.ValidationModule.EnableRuntimeRuleCache property to enable Rule caching for all persistent Rule Sources. You can also disable automatic collection of persistent Rules and Rule Sources and add custom proxy Rule Sources with different behavior. To see the example of how to do this, refer to the following property description: @DevExpress.ExpressApp.Validation.ValidationModule.EnableRuntimeRuleDiscovery.

## Example 
The following example demonstrates how to create a custom persistent Validation Rule Source:

1. Create a new class (**RuleRequiredFieldPersistent**) and implement the **IRuleSource** interface in it.
2. Apply @DevExpress.Persistent.Base.DefaultClassOptionsAttribute to this class to allow users to create Validation Rules at runtime.
3. In the [IRuleSource.CreateRules](xref:DevExpress.Persistent.Validation.IRuleSource.CreateRules) method, create a **RuleRequiredField** Validation Rule based on the values of the **RuleRequiredFieldPersistent** class public properties.

# [C# (EF Core)](#tab/tabid-csharp-efcore)

```csharp
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl.EF;
using DevExpress.Persistent.Validation;
using System;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations.Schema;
using System.Linq;
using System.Reflection;

namespace YourSolutionName.Module.BusinessObjects;
[DefaultClassOptions]
public class RuleRequiredFieldPersistent : BaseObject, IRuleSource {
    public virtual string RuleName { get; set; }
    public virtual string CustomMessageTemplate { get; set; }
    public virtual bool SkipNullOrEmptyValues { get; set; }
    public virtual bool InvertResult { get; set; }
    public virtual string ContextIDs { get; set; }

    public virtual string Property { get; set; }
    public virtual string ObjectType {
        get {
            if(ObjectTypeCore != null) {
                return ObjectTypeCore.FullName;
            }
            return "";
        }
        set { ObjectTypeCore = ReflectionHelper.FindType(value); }
    }
    [NotMapped]
    [TypeConverter(typeof(LocalizedClassInfoTypeConverter))]
    public virtual Type ObjectTypeCore { get; set; }
    #region IRuleSource Members
    public ICollection<IRule> CreateRules() {
        List<IRule> list = new List<IRule>();
        RuleRequiredField rule = new RuleRequiredField();
        rule.Properties.SkipNullOrEmptyValues = SkipNullOrEmptyValues;
        rule.Properties.Id = ID.ToString();
        rule.Properties.InvertResult = InvertResult;
        rule.Properties.CustomMessageTemplate = CustomMessageTemplate;
        rule.Properties.TargetContextIDs = ContextIDs;
        rule.Properties.TargetType = ObjectTypeCore;
        if(rule.Properties.TargetType != null) {
            foreach(PropertyInfo pi in rule.Properties.TargetType.GetProperties()) {
                if(pi.Name == Property) {
                    rule.Properties.TargetPropertyName = pi.Name;
                }
            }
        }
        for(int i = Validator.RuleSet.RegisteredRules.Count - 1; i >= 0; i--) {
            if(Validator.RuleSet.RegisteredRules[i].Id == ID.ToString()) {
                Validator.RuleSet.RegisteredRules.RemoveAt(i);
            }
        }
        list.Add(rule);
        return list;
    }
    [Browsable(false)]
    public string Name {
        get { return RuleName; }
    }
    #endregion
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Reflection;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl;
using DevExpress.Persistent.Validation;
using DevExpress.Xpo;
// ...
[DefaultClassOptions]
public class RuleRequiredFieldPersistent : BaseObject, IRuleSource {
    public RuleRequiredFieldPersistent(Session session) : base(session) { }
    public string RuleName {
        get { return GetPropertyValue<string>(nameof(RuleName)); }
        set { SetPropertyValue(nameof(RuleName), value); }
    }
    public string CustomMessageTemplate {
        get { return GetPropertyValue<string>(nameof(CustomMessageTemplate)); }
        set { SetPropertyValue(nameof(CustomMessageTemplate), value); }
    }
    public bool SkipNullOrEmptyValues {
        get { return GetPropertyValue<bool>(nameof(SkipNullOrEmptyValues)); }
        set { SetPropertyValue(nameof(SkipNullOrEmptyValues), value); }
    }
    public string Id {
        get { return GetPropertyValue<string>(nameof(Id)); }
        set { SetPropertyValue(nameof(Id), value); }
    }
    public bool InvertResult {
        get { return GetPropertyValue<bool>(nameof(InvertResult)); }
        set { SetPropertyValue(nameof(InvertResult), value); }
    }
    public string ContextIDs {
        get { return GetPropertyValue<string>(nameof(ContextIDs)); }
        set { SetPropertyValue(nameof(ContextIDs), value); }
    }
    public string Property {
        get { return GetPropertyValue<string>(nameof(Property)); }
        set { SetPropertyValue(nameof(Property), value); }
    }
    [Persistent("ObjectType")]
    protected string ObjectType {
        get {
            if (ObjectTypeCore != null) {
                return ObjectTypeCore.FullName;
            }
            return "";
        }
        set { ObjectTypeCore = ReflectionHelper.FindType(value); }
    }
    [NonPersistent]
    [TypeConverter(typeof(LocalizedClassInfoTypeConverter))]
    public Type ObjectTypeCore {
        get { return GetPropertyValue<Type>(nameof(ObjectTypeCore)); }
        set { SetPropertyValue(nameof(ObjectTypeCore), value); }
    }
    #region IRuleSource Members
    public ICollection<IRule> CreateRules() {
        List<IRule> list = new List<IRule>();
        RuleRequiredField rule = new RuleRequiredField();
        rule.Properties.SkipNullOrEmptyValues = this.SkipNullOrEmptyValues;
        rule.Properties.Id = this.Id;
        rule.Properties.InvertResult = this.InvertResult;
        rule.Properties.CustomMessageTemplate = this.CustomMessageTemplate;
        rule.Properties.TargetContextIDs = this.ContextIDs;
        rule.Properties.TargetType = this.ObjectTypeCore;
        if (rule.Properties.TargetType != null) {
            foreach (PropertyInfo pi in rule.Properties.TargetType.GetProperties()) {
                if (pi.Name == this.Property) {
                    rule.Properties.TargetPropertyName = pi.Name;
                }
            }
        }
        for (int i = Validator.RuleSet.RegisteredRules.Count - 1; i >= 0; i--) {
            if (Validator.RuleSet.RegisteredRules[i].Id == this.Id) {
                Validator.RuleSet.RegisteredRules.RemoveAt(i);
            }
        }
        list.Add(rule);
        return list;
    }
    [Browsable(false)]
    public string Name {
        get { return this.RuleName; }
    }
    #endregion
}
```

# [VB.NET (XPO)](#tab/tabid-vb-xpo)

```vb
Imports System
Imports System.Collections.Generic
Imports System.ComponentModel
Imports System.Reflection
Imports DevExpress.Persistent.Base
Imports DevExpress.Persistent.BaseImpl
Imports DevExpress.Persistent.Validation
Imports DevExpress.Xpo
' ...
<DefaultClassOptions>
Public Class RuleRequiredFieldPersistent
    Inherits BaseObject
    Implements IRuleSource

    Public Sub New(ByVal session As Session)
        MyBase.New(session)
    End Sub
    Public Property RuleName() As String
        Get
            Return GetPropertyValue(Of String)(NameOf(RuleName))
        End Get
        Set(ByVal value As String)
            SetPropertyValue(NameOf(RuleName), value)
        End Set
    End Property
    Public Property CustomMessageTemplate() As String
        Get
            Return GetPropertyValue(Of String)(NameOf(CustomMessageTemplate))
        End Get
        Set(ByVal value As String)
            SetPropertyValue(NameOf(CustomMessageTemplate), value)
        End Set
    End Property
    Public Property SkipNullOrEmptyValues() As Boolean
        Get
            Return GetPropertyValue(Of Boolean)(NameOf(SkipNullOrEmptyValues))
        End Get
        Set(ByVal value As Boolean)
            SetPropertyValue(NameOf(SkipNullOrEmptyValues), value)
        End Set
    End Property
    Public Property Id() As String
        Get
            Return GetPropertyValue(Of String)(NameOf(Id))
        End Get
        Set(ByVal value As String)
            SetPropertyValue(NameOf(Id), value)
        End Set
    End Property
    Public Property InvertResult() As Boolean
        Get
            Return GetPropertyValue(Of Boolean)(NameOf(InvertResult))
        End Get
        Set(ByVal value As Boolean)
            SetPropertyValue(NameOf(InvertResult), value)
        End Set
    End Property
    Public Property ContextIDs() As String
        Get
            Return GetPropertyValue(Of String)(NameOf(ContextIDs))
        End Get
        Set(ByVal value As String)
            SetPropertyValue(NameOf(ContextIDs), value)
        End Set
    End Property
    Public Property [Property]() As String
        Get
            Return GetPropertyValue(Of String)(NameOf([Property]))
        End Get
        Set(ByVal value As String)
            SetPropertyValue(NameOf([Property]), value)
        End Set
    End Property
    <Persistent("ObjectType")>
    Protected Property ObjectType() As String
        Get
            If ObjectTypeCore IsNot Nothing Then
                Return ObjectTypeCore.FullName
            End If
            Return ""
        End Get
        Set(ByVal value As String)
            ObjectTypeCore = ReflectionHelper.FindType(value)
        End Set
    End Property
    <NonPersistent, TypeConverter(GetType(LocalizedClassInfoTypeConverter))>
    Public Property ObjectTypeCore() As Type
        Get
            Return GetPropertyValue(Of Type)(NameOf(ObjectTypeCore))
        End Get
        Set(ByVal value As Type)
            SetPropertyValue(NameOf(ObjectTypeCore), value)
        End Set
    End Property
#Region "IRuleSource Members"
    Public Function CreateRules() As ICollection(Of IRule) _
    Implements IRuleSource.CreateRules
        Dim list As New List(Of IRule)()
        Dim rule As New RuleRequiredField()
        rule.Properties.SkipNullOrEmptyValues = Me.SkipNullOrEmptyValues
        rule.Properties.Id = Me.Id
        rule.Properties.InvertResult = Me.InvertResult
        rule.Properties.CustomMessageTemplate = Me.CustomMessageTemplate
        rule.Properties.TargetContextIDs = Me.ContextIDs
        rule.Properties.TargetType = Me.ObjectTypeCore
        If rule.Properties.TargetType IsNot Nothing Then
            For Each pi As PropertyInfo In rule.Properties.TargetType.GetProperties()
                If pi.Name = Me.Property Then
                    rule.Properties.TargetPropertyName = pi.Name
                End If
            Next pi
        End If
        For i As Integer = Validator.RuleSet.RegisteredRules.Count - 1 To 0 Step -1
            If Validator.RuleSet.RegisteredRules(i).Id = Me.Id Then
                Validator.RuleSet.RegisteredRules.RemoveAt(i)
            End If
        Next i
        list.Add(rule)
        Return list
    End Function
    <Browsable(False)>
    Public ReadOnly Property Name() As String _
    Implements IRuleSource.Name
        Get
            Return Me.RuleName
        End Get
    End Property
#End Region
End Class
```

***

## Limitations

- [Multitenant applications](xref:404436) do not currently support persistent validation rules.