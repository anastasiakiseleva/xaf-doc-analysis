---
uid: "113345"
seealso:
- linkId: "113218"
- linkId: "113294"
title: 'Test Conditional Appearance Rules'
---
# Test Conditional Appearance Rules

The [EasyTest](xref:113211) functional testing framework allows you to test [Conditional Appearance](xref:113286) rules. This topic demonstrates how to implement such tests.

To see beginner's step-by-step testing instructions, refer to the [Test an Action](xref:113218) topic.

Suppose you have the **MyPerson** persistent object that exposes the **Name**, **IsMarried** and **SpouseName** properties. The requirement is that the **SpouseName** property's editor is disabled when **IsMarried** is false. To do this, apply the [](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute) to the **SpouseName** property:

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
using DevExpress.ExpressApp.ConditionalAppearance;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl.EF;
using System.ComponentModel.DataAnnotations;
// ...
[DefaultClassOptions]
public class MyPerson : BaseObject {
    public virtual string Name { get; set; }

    private bool isMarried;
    [ImmediatePostData]
    public virtual bool IsMarried {
        get => isMarried;
        set {
            isMarried = value;
            if (!string.IsNullOrEmpty(SpouseName) && !value) SpouseName = string.Empty;
        }
    }

    [Appearance("DisableSpouseName", Criteria = "!IsMarried", Enabled = false)]
    public virtual string SpouseName { get; set; }
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp
using DevExpress.ExpressApp.ConditionalAppearance;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl;
using DevExpress.Xpo;
// ...
[DefaultClassOptions]
public class MyPerson : BaseObject {
    public MyPerson(Session session) : base(session) { }

    private string name;
    public string Name {
        get => name;
        set => SetPropertyValue(nameof(Name), ref name, value);
    }

    private bool isMarried;
    [ImmediatePostData]
    public bool IsMarried {
        get => isMarried;
        set {
            SetPropertyValue(nameof(IsMarried), ref isMarried, value);
            if (!string.IsNullOrEmpty(SpouseName) && !value) SpouseName = string.Empty;
        }
    }

    private string spouseName;
    [Appearance("DisableSpouseName", Criteria = "!IsMarried", Enabled = false)]
    public string SpouseName {
        get => spouseName;
        set => SetPropertyValue(nameof(SpouseName), ref spouseName, value);
    }
}
```

# [VB.NET (XPO)](#tab/tabid-vb-xpo)

```vb
Imports DevExpress.ExpressApp.ConditionalAppearance
Imports DevExpress.Persistent.Base
Imports DevExpress.Persistent.BaseImpl
Imports DevExpress.Xpo

' ...
<DefaultClassOptions>
Public Class MyPerson
    Inherits BaseObject

    Public Sub New(ByVal session As Session)
        MyBase.New(session)
    End Sub

    Private nameField As String

    Public Property Name As String
        Get
            Return nameField
        End Get
        Set(ByVal value As String)
            SetPropertyValue(NameOf(MyPerson.Name), nameField, value)
        End Set
    End Property

    Private isMarriedField As Boolean

    <ImmediatePostData>
    Public Property IsMarried As Boolean
        Get
            Return isMarriedField
        End Get
        Set(ByVal value As Boolean)
            SetPropertyValue(NameOf(MyPerson.IsMarried), isMarriedField, value)
            If Not String.IsNullOrEmpty(SpouseName) AndAlso Not value Then SpouseName = String.Empty
        End Set
    End Property

    Private spouseNameField As String

    <Appearance("DisableSpouseName", Criteria:="!IsMarried", Enabled:=False)>
    Public Property SpouseName As String
        Get
            Return spouseNameField
        End Get
        Set(ByVal value As String)
            SetPropertyValue(NameOf(MyPerson.SpouseName), spouseNameField, value)
        End Set
    End Property
End Class
```

***

![TestConditionalAppearanceRules](~/images/testconditionalappearancerules116897.png)

To test the **MyPerson** object's Conditional Appearance rule, you can use the following EasyTest script.

# [ETS](#tab/tabid-ets)

```ETS
;#DropDB MySolutionEasyTest

#Application MySolutionWin
#Application MySolutionWeb
#Application MySolutionBlazor

*Action Navigation(Person)

*Action New

;Set IsMarried to true
*FillForm
 Name = Jane Smith
 Is Married = true

;Test that the SpouseName field is editable
*FillForm
 Spouse Name = John Smith

;Set IsMarried to false
*FillForm
 Is Married = false

;Test that the SpouseName field is not editable
!FillForm
 Spouse Name = John Smith
```
***


> [!NOTE]
> EasyTest supports only test visibility and an enabled/disabled state.
