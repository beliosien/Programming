#include "TreeNode.h"

template<typename T>
Tree<T>::Tree(T item)
{
	this->root_ = new TreeNode(item, nullptr, nullptr);
	this->size_ = 0;
}


template<typename T>
Tree<T>::~Tree()
{
	if (this->size_ > 0) this.clear()
}

template<typename T>
Tree<T>::TreeNode::TreeNode(T item, Tree* left, Tree* right): item_(item), left_(left), right_(right)
{
}

template<typename T>
Tree<T>::TreeNode::~TreeNode()
{
	delete left_;
	delete right_;
}

template<typename T>
void Tree<T>::clear()
{
}

template<typename T>
Tree<T>::TreeNode* Tree<T>::getRoot()
{
	return this->root_;
}

template<typename T>
int Tree<T>::getSize()
{
	return this->size;
}

template<typename T>
void Tree<T>::addTreeNode(TreeNode* root, T item)
{
	if (root == nullptr)
	{
		root = new TreeNode(item, nullptr, nullptr);
		this->size_++;
		return;
	}

	if (root->getLeft() != nullptr)
	{
		addTreeNode(root->getLeft(), item);
	}
	else
	{
		root->setLeft(new TreeNode(item, nullptr, nullptr);
		this->size_++;
		return;
	}

	if (root->getRight() != nullptr)
	{
		addTreeNode(root->getRight(), item);
	}
	else
	{
		root->setRight(new TreeNode(item, nullptr, nullptr);
		this->size_++;
		return;
	}
}

template<typename T>
void Tree<T>::deleteTreeNode(TreeNode* node, T item)
{
	if (node->getItem() == item)
	{
		delete node;
	}
}

template<typename T>
T& Tree<T>::TreeNode::getItem()
{
	return this->item_;
}

template<typename T>
void Tree<T>::TreeNode::setLeft(TreeNode* treeNode)
{
	this->left_ = treeNode;
}

template<typename T>
void Tree<T>::TreeNode::setRight(TreeNode* treeNode)
{
	this->right_ = treeNode;
}

template<typename T>
Tree<T>::TreeNode* Tree<T>::TreeNode::getRight()
{
	return this->right_;
}

template<typename T>
Tree<T>::TreeNode* Tree<T>::TreeNode::getLeft()
{
	return this->left_;
}



