#include <opencv2/core/core.hpp>
#include <opencv2/photo/photo.hpp>
#include <opencv2/video/video.hpp>
#include <opencv2/highgui/highgui.hpp>

#include <iostream>
#include <cstdlib>
#include <string>

using namespace cv;
using cv::CLAHE;

int main(int argc, const char** argv) {

  VideoCapture cap;

  if(argc > 1)
  {
    cap = VideoCapture(argv[1]);
  }
  else
  {
    return EXIT_SUCCESS;
  }

  if(!cap.isOpened())
  {
    std::cout << "Cannot open video" << std::endl;
    return EXIT_FAILURE;
  }

  double fps = cap.get(CV_CAP_PROP_FPS);
  int width = cap.get(CV_CAP_PROP_FRAME_WIDTH); 
  int height = cap.get(CV_CAP_PROP_FRAME_HEIGHT);

  std::cout << "FPS=" << fps << std::endl;  
  std::cout << "WIDTH=" << width  << std::endl;
  std::cout << "HEIGHT=" << height << std::endl;

  Size frameSize(width, height);

  VideoWriter output("genVid.avi", CV_FOURCC('P','I','M','1'), 20,
		     frameSize, false);

  if(!output.isOpened())
  {
    std::cout << "error opening file for writing" << std::endl;
  }
  
  string winName("Test");
  string bwName("bw");

  namedWindow(winName, CV_WINDOW_AUTOSIZE);
  namedWindow(bwName, CV_WINDOW_AUTOSIZE);

  while(1)
  {
    Mat frame;

    cap >> frame;
    if(frame.empty())
    {
      std::cout << "Frame error" << std::endl;
      break;
    }
    Mat bw_frame(frameSize, CV_8UC1, Scalar(0));
    Mat bw_clahed(frameSize, CV_8UC1, Scalar(0));
    cvtColor(frame, bw_frame, CV_RGB2GRAY);

    Ptr<CLAHE> clahe = createCLAHE();
    clahe->apply(bw_frame, bw_clahed);

    imshow(winName, frame);
    imshow(bwName, bw_clahed);

    output << bw_clahed;

    if(waitKey(30) == 27 )
    {
      std::cout << "Exiting by user intervention" << std::endl;
      break;
    }
  }

  return EXIT_SUCCESS;
}
