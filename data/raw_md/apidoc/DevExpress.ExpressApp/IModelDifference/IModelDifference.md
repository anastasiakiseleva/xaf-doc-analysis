---
uid: DevExpress.ExpressApp.IModelDifference
name: IModelDifference
type: Interface
summary: Declares members implemented by entities (persistent classes) used to [store model differences](xref:403527) in the database.
syntax:
  content: public interface IModelDifference
seealso:
- linkId: DevExpress.ExpressApp.IModelDifference._members
  altText: IModelDifference Members
---
When model differences are stored in the database, each user has the associated **IModelDifference** object. The [IModelDifference.UserId](xref:DevExpress.ExpressApp.IModelDifference.UserId) property specifies the identifier of the user who owns the current **IModelDifference** object. If the **UserId** is not specified, the current **IModelDifference** object specifies the model differences layer shared by all users (administrator model differences). The [IModelDifference.Aspects](xref:DevExpress.ExpressApp.IModelDifference.Aspects) property exposes the list of model difference aspects ([](xref:DevExpress.ExpressApp.IModelDifferenceAspect) objects). The aspect with an empty [IModelDifferenceAspect.Name](xref:DevExpress.ExpressApp.IModelDifferenceAspect.Name) property is the default culture-neutral aspect. Aspects with the **Name** set to a certain [language code](https://learn.microsoft.com/en-us/dotnet/api/system.globalization.cultureinfo) are used in [localized](xref:113298) applications. The XML code of a particular model difference aspect is available via the [IModelDifferenceAspect.Xml](xref:DevExpress.ExpressApp.IModelDifferenceAspect.Xml) property.

The [](xref:DevExpress.Persistent.BaseImpl.ModelDifference) class from the [](xref:DevExpress.Persistent.BaseImpl) namespace is a built-in implementation of this interface that can be used in XPO applications. In Entity Framework applications, the similar [](xref:DevExpress.Persistent.BaseImpl.EF.ModelDifference) entity from the [](xref:DevExpress.Persistent.BaseImpl.EF) namespace can be used.

To create a custom persistent container for the model differences, do the following:

* Implement the **IModelDifference**  and [](xref:DevExpress.ExpressApp.IModelDifferenceAspect) interfaces.
* Establish the _one-to-many_ association between these classes using the [IModelDifference.Aspects](xref:DevExpress.ExpressApp.IModelDifference.Aspects) and [IModelDifferenceAspect.Owner](xref:DevExpress.ExpressApp.IModelDifferenceAspect.Owner) properties.
* Pass the implemented **IModelDifference** type to the **ModelDifferenceDbStorage** constructor, as demonstrated in the [How to: Store the Application Model Differences in the Database](xref:113698) topic.
