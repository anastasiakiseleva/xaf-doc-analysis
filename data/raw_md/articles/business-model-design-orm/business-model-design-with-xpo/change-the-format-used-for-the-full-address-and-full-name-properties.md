---
uid: "113173"
seealso:
- linkId: DevExpress.ExpressApp.Xpo.CalculatedPersistentAliasAttribute
title: 'Change the Format Used for the FullAddress and FullName Properties'
owner: Ekaterina Kiseleva
---
# Change the Format Used for the FullAddress and FullName Properties

There are FullAddress and FullName properties in the Address and Person business classes that are supplied with the [Business Class Library](xref:112571). These properties are calculable. The FullAddress property represents a string formed by the concatenation of the Country.Name, StateProvince, City, Street and ZipPostal property values. The FullName property is formed by the concatenation of the FirstName, MiddleName and LastName property values. The FullAddress and FullName properties are implemented so that you can change the order in which the items are concatenated. This topic details how to change this order. You can use this technique when implementing analogous business class properties.

The following images demonstrate how the FullAddress and FullName properties are calculated.

![FullAddress](~/images/fulladdress116257.png)

![FullName](~/images/fullname116258.png)

To format FullAddress and FullName properties, the [ObjectFormatter.Format](xref:DevExpress.Persistent.Base.ObjectFormatter.Format*) method of the helper [](xref:DevExpress.Persistent.Base.ObjectFormatter) class is used. In this method, the format, according to which the property value is generated, is taken as a parameter. The format passed for the FullAddress property is specified by the Address class' **FullAddressFormat** property. The format that is passed for the FullName property is specified by the Person class' **FullNameFormat** property. Note that FullAddress and FullName properties are non-persistent calculated properties. As such, they require persistent aliases to be created for them to support sorting in [Server, ServerView, InstantFeedback, and InstantFeedbackView](xref:118450) mode (see [CollectionSourceBase.DataAccessMode](xref:DevExpress.ExpressApp.CollectionSourceBase.DataAccessMode)). For this purpose, there are additional FullNamePersistentAlias and FullAddressPersistentAlias properties. These properties are used to create persistent aliases.

By default, the **FullAddressFormat** property is set to the Address class' **defaultFullAddressFormat** constant, which is the following: "{Country.Name}; {StateProvince}; {City}; {Street}; {ZipPostal}". The **FullAddressFormatPersistentAlias** property is set to the Address class' **defaultFullAddressPersistentAlias** constant, which is the following: "concat(Country.Name, StateProvince, City, Street, ZipPostal)". To change these property values, use the **SetFullAddressFormat** method (**SetFullNameFormat** for the Person class). These methods are static, so you can call them any place in your solution. For instance, you can specify the required format in the configuration file and read its value in a module's constructor. In addition, override the module's [ModuleBase.CustomizeTypesInfo](xref:DevExpress.ExpressApp.ModuleBase.CustomizeTypesInfo(DevExpress.ExpressApp.DC.ITypesInfo)) method and process the **CalculatedPersistentAlias** attribute via the static **CalculatedPersistentAliasHelper.CustomizeTypesInfo** method.

# [XML](#tab/tabid-xml)

```XML
<configuration>
    <appSettings>
        <add key="FullAddressFormat" value="{Country.Name} {City} {Street}" />
        <add key="FullAddressFormatPersistentAlias" value="concat(Country.Name, City, Street)" />
        <!-- ... -->
    </appSettings>
</configuration>
```

***

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.Persistent.BaseImpl;
using System.Configuration;
//...
public sealed partial class MainDemoModule : ModuleBase {
    static MainDemoModule() {
        Address.SetFullAddressFormat(ConfigurationManager.AppSettings["FullAddressFormat"], 
            ConfigurationManager.AppSettings["FullAddressFormatPersistentAlias"]);
    }
    public override void CustomizeTypesInfo(ITypesInfo typesInfo) {
        base.CustomizeTypesInfo(typesInfo);
        CalculatedPersistentAliasHelper.CustomizeTypesInfo(typesInfo);
    }
    //...
}
```
***

After formatting a FullAddress property using the specified format, the property names that are enclosed in curly brackets will be replaced with the current object's property values (see the image above).

Analogous to the Address class' **FullAddressFormat** property, the Person class' **FullNameFormat** property is set to the **defaultFullNameFormat** constant, which is the following: "{FirstName} {MiddleName} {LastName}". The **FullNamePersistentAlias** property is set to the **defaultFullNamePersistentAlias** constant, which is the following: "concat(FirstName, MiddleName, LastName)". As the **SetFullNameFormat** method is static, you are free to call it where required. For instance, you can use the value specified in the configuration file as demonstrated in the code above.

> [!NOTE]
> In the Main Demo, you can set a custom format for the FullName property in the common module's constructor, as described above.

When implementing business class properties whose values require formatting, introduce static properties like FullAddressFormat and FullNameFormat, so that anyone using your business class can modify the formatting. The following code can be used as an example:

# [C#](#tab/tabid-csharp)

```csharp
public class SampleAddress : BaseObject {
    private const string defaultFullAddressFormat = "{Country.Name}; {StateProvince};" +
       " {City}; {Street}; {ZipPostal}";
    private static string fullAddressFormat = defaultFullAddressFormat;
    public static string FullAddressFormat {
        get { return fullAddressFormat; }
        set {
            fullAddressFormat = value;
            if(string.IsNullOrEmpty(fullAddressFormat)) {
                fullAddressFormat = defaultFullAddressFormat;
            }
        }
    }
    public string FullAddress {
        get {
            return ObjectFormatter.Format(fullAddressFormat, this, 
               EmptyEntriesMode.RemoveDelimiterWhenEntryIsEmpty );
        }
    }
}
```
***