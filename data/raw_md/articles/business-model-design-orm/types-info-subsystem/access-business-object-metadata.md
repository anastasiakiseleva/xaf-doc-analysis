---
uid: "113224"
seealso: []
title: Access Business Object Metadata
---
# Access Business Object Metadata

This topic explains how the [Types Info Subsystem](xref:113669) can be used in your applications.

Business class metadata can be accessed via the static **Instance** property of the **XafTypesInfo** class. This property returns an **ITypesInfo** object, which represents metadata on all business classes used in an **XAF** application.
To get metadata on a particular entity, perform the following steps:

1. Access the **XafTypesInfo.Instance** property to get an **ITypesInfo** object.
	
	``XafTypesInfo.Instance``
2. To get metadata on a business class, use the [ITypesInfo.FindTypeInfo](xref:DevExpress.ExpressApp.DC.ITypesInfo.FindTypeInfo*) method.
	
	``XafTypesInfo.Instance.FindTypeInfo(ObjectType)``
    
    This method returns an **ITypeInfo** object.
3. To get metadata on a business class member, use the **ITypeInfo** object's [ITypeInfo.FindMember](xref:DevExpress.ExpressApp.DC.ITypeInfo.FindMember(System.String)) method.
	
	``XafTypesInfo.Instance.FindTypeInfo(ObjectType).FindMember(PropertyName)``
    
    This method returns an **IMemberInfo** object.
4. To get specific information, use the properties of the **ITypeInfo** or **IMemberInfo** object. The **ITypeInfo** object provides information about a type, and the **IMemberInfo** object provides information about a member.

	``XafTypesInfo.Instance.FindTypeInfo(ObjectType).IsAbstract``
	 
	``XafTypesInfo.Instance.FindTypeInfo(ObjectType).FindMember(PropertyName).IsList``

The types info interfaces declare many properties and methods that supply metadata. To learn about the metadata the types info subsystem supplies, refer to the member list of each interface.

In addition to the **XafTypesInfo** class, many **XAF** classes supply metadata associated with them. For instance, Property Collection Sources have the [PropertyCollectionSource.MemberInfo](xref:DevExpress.ExpressApp.PropertyCollectionSource.MemberInfo) property, which supplies metadata on a property represented by the Collection Source. Another example is a [View](xref:112611) that exposes the [ObjectView.ObjectTypeInfo](xref:DevExpress.ExpressApp.ObjectView.ObjectTypeInfo) property, supplying metadata on the type of represented objects.

Below is an example on how to utilize the metadata supplied by the types info subsystem. In the code snippet, a [View Controller](xref:112621) checks whether or not a business class has a custom **MyAttribute** attribute applied. If the attribute is applied, then the custom code is executed when the Controller is activated.

# [C#](#tab/tabid-csharp)

```csharp
//...
[AttributeUsage(AttributeTargets.Class, Inherited = false)]
public class MyCustomAttribute : Attribute { }

[MyCustomAttribute]
public class DemoContact : BaseObject {
//...
}

//...
public partial class MyViewController : ViewController {
    //...
    private void MyViewController_Activated(object sender, EventArgs e) {
        if (View.ObjectTypeInfo.FindAttribute<MyCustomAttribute>() != null) {
            // Place your code here.
        }
    }
}
```
***

> [!NOTE]
> In this code, **DemoContact** is an XPO class, but it can be an Entity Framework entity class as well. The **MyViewController** Controller operates in the same way in all of these cases.

Another situation when you may need to access the types info subsystem is when you need to add an attribute to a class or member from an external class library. Refer to the [How to customize a Business Model at runtime](https://supportcenter.devexpress.com/ticket/details/e250/xaf-customize-an-xpo-business-model-at-runtime) example for details.
