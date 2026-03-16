---
uid: DevExpress.ExpressApp.BaseObjectSpace.FirstOrDefault``1(System.Linq.Expressions.Expression{System.Func{``0,System.Boolean}})
name: FirstOrDefault<ObjectType>(Expression<Func<ObjectType, Boolean>>)
type: Method
summary: Searches for the first object that matches the specified lambda expression. The generic parameter determines the object's type.
syntax:
  content: |-
    public ObjectType FirstOrDefault<ObjectType>(Expression<Func<ObjectType, bool>> criteriaExpression)
        where ObjectType : class
  parameters:
  - id: criteriaExpression
    type: System.Linq.Expressions.Expression{System.Func{{ObjectType},System.Boolean}}
    description: A lambda expression to search for an object.
  typeParameters:
  - id: ObjectType
    description: The @System.Type of an object to be returned.
  return:
    type: '{ObjectType}'
    description: The first object that matches the specified lambda expression.
seealso: []
---
This method invokes the public virtual @DevExpress.ExpressApp.BaseObjectSpace.FirstOrDefault``1(System.Linq.Expressions.Expression{System.Func{``0,System.Boolean}},System.Boolean) method that does nothing and returns `null`. Override this virtual method in a `BaseObjectSpace` descendant to implement an object search.