#pragma once

/**
		@author:  Ossim Belias
		@Description: Implementation of own Tree class
*/


template <typename T>
class Tree
{
public:
	// constructor 
	Tree(T item);
	// destructor
	~Tree();

	class TreeNode
	{
	public:
		// constructor
		TreeNode(T item, Tree* left, Tree* right);
		// destructor 
		~TreeNode();

		// retrun the item 
		T& getItem();
		// set the left node
		void setLeft(TreeNode* treeNode);
		// set the right node
		void setRight(TreeNode* treeNode);
		// return the right tree node
		TreeNode* getRight();
		// return the left tree node
		TreeNode* getLeft();

	private:
		T item_;
		TreeNode* left_;
		TreeNode* right_;
	};

	// clear the tree
	void clear();
	// return the root
	TreeNode* getRoot();
	// return the size
	int getSize();
	// add tree node
	void addTreeNode(TreeNode* root,T item);
	// delete tree node
	void deleteTreeNode(TreeNode* node,T item);

private:
	TreeNode* root_;
	int size_; 
};

