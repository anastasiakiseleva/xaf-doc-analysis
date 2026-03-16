---
uid: "113669"
seealso:
- linkType: HRef
  linkId: https://supportcenter.devexpress.com/ticket/details/e250/xaf-customize-an-xpo-business-model-at-runtime
  altText: How to customize an XPO business model at runtime
title: Types Info Subsystem
owner: Ekaterina Kiseleva
---
# Types Info Subsystem

The majority of the [Application Model](xref:112580) is generated based on the business classes used in an **XAF** application. To generate the Application Model, business class metadata is required. In **XAF**, this metadata is supplied by the types info subsystem, which is a set of classes and interfaces specifically designed to supply business class metadata.

The types info subsystem is presented by the static **XafTypesInfo** class, declared in the **DevExpress.ExpressApp** namespace, and the following interfaces.

| Interface | Description |
|---|---|
| [](xref:DevExpress.ExpressApp.DC.IBaseInfo) | The base interface that supplies metadata on business classes and their members. |
| [](xref:DevExpress.ExpressApp.DC.IMemberInfo) | Supplies metadata on a member of a business class. |
| [](xref:DevExpress.ExpressApp.DC.ITypeInfo) | Supplies metadata on a business class. |
| [](xref:DevExpress.ExpressApp.DC.ITypesInfo) | Supplies metadata on business classes used by an **XAF** application. |
| [](xref:DevExpress.ExpressApp.DC.IAssemblyInfo) | Supplies metadata on an assembly used by an **XAF** application. |

You do not need to implement these interfaces in most cases. These interfaces are implemented by a number of **XAF** system classes that can be accessed from different parts of your application. All of the mentioned interfaces are interlinked. For instance, if you have an **ITypesInfo** object, you can get information on any business class and its members, or the assembly in which it is declared. If you have an **IMemberInfo** object describing a property, you can get metadata on the assembly in which the property's owner type is declared.

[comment]: <> (<\!--<para>The entry point for the Types Info customization is the <see cref="M:DevExpress.ExpressApp.ModuleBase.CustomizeTypesInfo"/> method. If you override this method in your module, you can access the <see cref="T:DevExpress.ExpressApp.DC.ITypesInfo"/> instance passed to this method.</para>-->)

To learn more about the **Types Info Subsystem**, refer to the following topics.

* [Access Business Object Metadata](xref:113224)
* [Use Metadata to Customize Business Classes Dynamically](xref:113583)
