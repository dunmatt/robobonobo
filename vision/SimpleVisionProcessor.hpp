/* 
 * File:   SimpleVisionProcesor.hpp
 * Author: evan
 *
 * Created on July 2, 2014, 10:37 PM
 */

#ifndef SIMPLEVISIONPROCESOR_HPP
#define	SIMPLEVISIONPROCESOR_HPP


#include <pcl/io/openni_grabber.h>
// #include <pcl/visualization/cloud_viewer.h>
#include <pcl/segmentation/sac_segmentation.h>
#include <pcl/filters/voxel_grid.h>
#include <pcl/segmentation/extract_clusters.h>
#include <zmq.hpp>

class SimpleVisionProcessor {
public:

  SimpleVisionProcessor();
  ~SimpleVisionProcessor();

  void run();
  void stop();

private:
  void processCloud(const pcl::PointCloud<pcl::PointXYZ>::ConstPtr &cloud);
  void initParameters();
  void sendData();
  zmq::context_t context;
  zmq::socket_t mainAi;

  pcl::Grabber* interface;
  // pcl::visualization::CloudViewer viewer;

  pcl::VoxelGrid<pcl::PointXYZ> vox_grid;
  pcl::SACSegmentationFromNormals<pcl::PointXYZ, pcl::Normal> segmentation;
  pcl::EuclideanClusterExtraction<pcl::PointXYZ> euc_cluster;
};


#endif	/* SIMPLEVISIONPROCESOR_HPP */

