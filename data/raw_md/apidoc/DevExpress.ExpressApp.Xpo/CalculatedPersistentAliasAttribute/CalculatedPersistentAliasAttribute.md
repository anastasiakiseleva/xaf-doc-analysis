---
uid: DevExpress.ExpressApp.Xpo.CalculatedPersistentAliasAttribute
name: CalculatedPersistentAliasAttribute
type: Class
summary: Applied to a business class. Allows you to dynamically configure a persistent alias for the target business class' property.
syntax:
  content: |-
    [AttributeUsage(AttributeTargets.Class, AllowMultiple = true, Inherited = false)]
    public class CalculatedPersistentAliasAttribute : Attribute
seealso:
- linkId: DevExpress.ExpressApp.Xpo.CalculatedPersistentAliasAttribute._members
  altText: CalculatedPersistentAliasAttribute Members
- linkId: "113179"
---
Non-persistent calculated properties for which filtering and sorting should be performed on the database level can be implemented via the [](xref:DevExpress.Xpo.PersistentAliasAttribute). The **PersistentAlias** attribute takes a single parameter which specifies the expression used to calculate the property's value on the database server side. A persistent alias must be specified in code as the attribute's parameter. However, in certain scenarios, the property may be required to have a configurable persistent alias, and it must be possible to configure it in a deployed application by an administrator. In this instance, the **CalculatedPersistentAliasAttribute** attribute should be used.

The **CalculatedPersistentAliasAttribute** contains two properties initialized via the attribute's constructor. The first parameter specifies the property name for which you would like to set up a persistent alias. The second parameter specifies the property which returns the alias' expression. The property which returns the alias' expression can return different expressions based on a specific rule. For example, you can implement logic which loads the alias expression from a configuration file which can be customized by a system administrator.

Note that the **CalculatedPersistentAliasAttribute** attribute is initialized at the application startup, while the application is being set up. So, if you want to change the value returned by the property which specifies the alias expression, this should be done while the application is being initialized, for example, in a module's constructor.

The following code snippet illustrates use of the **CalculatedPersistentAliasAttribute**. The **Product** class contains the calculated **ProductName** property, which has a configurable persistent alias:

# [C#](#tab/tabid-csharp)

```csharp
[CalculatedPersistentAlias(nameof(ProductName), nameof(ProductNameAlias)), DefaultClassOptions]
public class Product : BaseObject {
    public Product(Session session) : base(session) { }

    private static string productNameFormat = "{Manufacturer} {Model}";
    private static string productNameAlias = "concat(Manufacturer, Model)";
        
    public string ProductName {
        get { return ObjectFormatter.Format(
            productNameFormat, this, EmptyEntriesMode.RemoveDelimiterWhenEntryIsEmpty ); }
    }
    [Browsable(false)]
    public static string ProductNameAlias {
        get { return productNameAlias; }            
    }
    public static void SetProductNameFormat(string productNameFormat, string productNameAlias) {
        if(!string.IsNullOrEmpty(productNameFormat)) {
            Product.productNameFormat = productNameFormat;
        }
        if(!string.IsNullOrEmpty(productNameAlias)) {
            Product.productNameAlias = productNameAlias;
        }
    }

    public string Manufacturer {
        get { return GetPropertyValue<string>(nameof(Manufacturer)); }
        set { SetPropertyValue<string>(nameof(Manufacturer), value); }
    }
    public string Model {
        get { return GetPropertyValue<string>(nameof(Model)); }
        set { SetPropertyValue<string>(nameof(Model), value); }
    }
    public string Revision {
        get { return GetPropertyValue<string>(nameof(Revision)); }
        set { SetPropertyValue<string>(nameof(Revision), value); }
    }
}
```
***

Note that a property which returns the persistent alias' expression must be declared as `public` and `static`.

The persistent alias' value is initialized from the application's configuration file in a module's constructor:

# [C#](#tab/tabid-csharp)

```csharp
public sealed partial class CalculatedAliasModule : ModuleBase {
    public CalculatedAliasModule() {
        InitializeComponent();
         
        Product.SetProductNameFormat(    
            ConfigurationManager.AppSettings["ProductNameFormat"],    
            ConfigurationManager.AppSettings[nameof(ProductNameAlias)]    
            );   
    }
}
```
***
In addition, it is required to override the [ModuleBase.CustomizeTypesInfo](xref:DevExpress.ExpressApp.ModuleBase.CustomizeTypesInfo(DevExpress.ExpressApp.DC.ITypesInfo)) method in the following manner:

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.Xpo;
// ...
public override void CustomizeTypesInfo(ITypesInfo typesInfo) {
    base.CustomizeTypesInfo(typesInfo);
    CalculatedPersistentAliasHelper.CustomizeTypesInfo(typesInfo);
}
```
***

Note that two business classes from the [Business Class Library](xref:112571) use the **CalculatedPersistentAliasAttribute** attribute. The **Person** class uses this attribute to configure the format of the calculated **FullName** property, and the **Address** class uses this attribute to configure the calculated **FullAddress** property. To learn how to configure the format of these properties, refer to the [How to: Change the Format Used for the FullAddress and FullName Properties](xref:113173) topic.
