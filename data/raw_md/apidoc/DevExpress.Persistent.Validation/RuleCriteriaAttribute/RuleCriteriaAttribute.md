---
uid: DevExpress.Persistent.Validation.RuleCriteriaAttribute
name: RuleCriteriaAttribute
type: Class
summary: Defines a validation rule that demands an object of the target type satisfy a specified criterion.
syntax:
  content: |-
    [AttributeUsage(AttributeTargets.Class | AttributeTargets.Property | AttributeTargets.Interface, AllowMultiple = true)]
    public class RuleCriteriaAttribute : RuleBaseAttribute, IRuleCriteriaProperties, IRuleCollectionPropertyProperties, IRuleBaseProperties
seealso:
- linkId: DevExpress.Persistent.Validation.RuleCriteriaAttribute._members
  altText: RuleCriteriaAttribute Members
- linkId: "113008"
---
Apply this attribute to a business class to define a criterion that must be satisfied by this class' objects. Use the _criteria_ parameter to specify the required criterion. To learn how to write criteria correctly, refer to the [Ways to Build Criteria](xref:113052) topic. In criteria, you can use [Function Criteria Operators](xref:113307). For instance, the "Today = LocalDateTimeToday()" criterion means that the Today property must be set to the current date.

When applying this attribute, use common parameters that are inherited from the [](xref:DevExpress.Persistent.Validation.RuleBaseAttribute) class, in addition to the _criteria_ parameter.

Note that when you need to check whether a property is specified, use the [](xref:DevExpress.Persistent.Validation.RuleRequiredFieldAttribute), rather than the **RuleCriteriaAttribute**. However, there are scenarios when you need to use the **RuleCriteriaAttribute** for this purpose. The following code demonstrates one of them. The Address objects are related to the User and Client objects by the One-To-One relationship. But, the Address object must not have the House property set to 0 when it is assigned to the Client objects.

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
[DefaultClassOptions]
public class Address : BaseObject {
    public virtual string Street { get; set; }
    public virtual int House { get; set; }
}

[DefaultClassOptions]
[RuleCriteria("", DefaultContexts.Save, "ClientAddress.House != 0",
   "House should not be 0", SkipNullOrEmptyValues = false)]
public class Client : BaseObject {
    public virtual string ClientName { get; set; }
    public virtual Address ClientAddress { get; set; }
}

[DefaultClassOptions]
public class User : BaseObject {
    public virtual string UserName { get; set; }
    public virtual Address UserAddress { get; set; }
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp
[DefaultClassOptions]
public class Address : BaseObject {
   public Address(Session session) : base(session) { }
   private string street;
   public string Street {
      get { return street; }
      set { SetPropertyValue(nameof(Street), ref street, value); }
   }
   private int house;
   public int House{
      get { return house; }
      set { SetPropertyValue(nameof(House), ref house, value); }
   }
}
[DefaultClassOptions]
[RuleCriteria("", DefaultContexts.Save, "ClientAddress.House != 0",
   "House should not be 0", SkipNullOrEmptyValues = false)]
public class Client : BaseObject {
   public Client(Session session) : base(session) { }
   string fClientName;
   public string ClientName {
       get { return fClientName; }
       set { SetPropertyValue(nameof(ClientName), ref fClientName, value); }
   }
   Address fClientAddress;
   public Address ClientAddress {
       get { return fClientAddress; }
       set { SetPropertyValue(nameof(ClientAddress), ref fClientAddress, value); }
   }
 }
[DefaultClassOptions]
public class User : BaseObject {
   public User(Session session) : base(session) { }
   string fUserName;
   public string UserName {
       get { return fUserName; }
       set { SetPropertyValue(nameof(UserName), ref fUserName, value); }
   }
   Address fUserAddress;
   public Address UserAddress {
       get { return fUserAddress; }
       set { SetPropertyValue(nameof(UserAddress), ref fUserAddress, value); }
   }
}
```

# [VB.NET (XPO)](#tab/tabid-vb-xpo)

```vb
<DefaultClassOptions> _
Public Class Address
      Inherits BaseObject
   Public Sub New(ByVal session As Session)
      MyBase.New(session)
   End Sub
   Private fstreet As String
   Public Property Street() As String
      Get
         Return fstreet
      End Get
      Set
         SetPropertyValue(NameOf(Street), fstreet, Value)
      End Set
   End Property
   Private fhouse As Integer
   Public Property House() As Integer
      Get
         Return fhouse
      End Get
      Set
         SetPropertyValue(NameOf(House), fhouse, Value)
      End Set
   End Property
End Class
<DefaultClassOptions, RuleCriteria("", DefaultContexts.Save, "ClientAddress.House != 0", _
   "House should not be 0", SkipNullOrEmptyValues := False)> _
Public Class Client
      Inherits BaseObject
   Public Sub New(ByVal session As Session)
      MyBase.New(session)
   End Sub
   Public Property ClientName() As String
       Get
           Return fClientName
       End Get
       Set(ByVal value as String)
           SetPropertyValue(NameOf(ClientName), fClientName, value)
       End Set
   End Property
   Private fClientName As String

   Public Property ClientAddress() As Address
       Get
           Return fClientAddress
       End Get
       Set(ByVal value as Address)
           SetPropertyValue(NameOf(ClientAddress), fClientAddress, value)
       End Set
   End Property
   Private fClientAddress As Address

End Class
<DefaultClassOptions> _
Public Class User
      Inherits BaseObject
   Public Sub New(ByVal session As Session)
      MyBase.New(session)
   End Sub
   Public Property UserName() As String
       Get
           Return fUserName
       End Get
       Set(ByVal value as String)
           SetPropertyValue(NameOf(UserName), fUserName, value)
       End Set
   End Property
   Private fUserName As String

   Public Property UserAddress() As Address
       Get
           Return fUserAddress
       End Get
       Set(ByVal value as Address)
           SetPropertyValue(NameOf(UserAddress), fUserAddress, value)
       End Set
   End Property
   Private fUserAddress As Address

End Class
```

***

In the code above, the **RuleCriteriaAttribute** has the [RuleBaseAttribute.SkipNullOrEmptyValues](xref:DevExpress.Persistent.Validation.RuleBaseAttribute.SkipNullOrEmptyValues) parameter set to **false**. This is required, so that the rule defined by this attribute is checked when the target property is not specified.

The rule generated by the **RuleCriteriaAttribute** will be loaded to the [Application Model](xref:112580)'s [](xref:DevExpress.ExpressApp.Validation.IModelValidationRules) node. So, you can customize this rule via the [Model Editor](xref:112582). In addition, you can create new rules in the Model Editor as well. For details, refer to the [](xref:402980) topic.

[!include[<**RuleCriteria** and other validation attributes>](~/templates/main-demo-tip.md)]